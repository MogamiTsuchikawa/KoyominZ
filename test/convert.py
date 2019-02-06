import wx,time,json,xmltodict
import xml.etree.ElementTree as ET
import const
#指定されたコントロールの種類の全部のプロパティを生成
#@numba.jit
def MakeCtrlProps_CS(ui_d, kind):
    output = ""
    
    ui_d_a = ui_d[kind]
    for ctrlname in ui_d_a:
        target = ui_d_a[ctrlname]
        #this.buttonExit = new System.Windows.Forms.Button();
        output += "            this.%s = new System.Windows.Forms.%s();\n" % (
            ctrlname, kind)
        output += "            this.%s.Name = \"%s\";\n" % (
            ctrlname, ctrlname)
        for prop_kind in target:
            rtn = GetProp_CS(prop_kind, target)
            if rtn != "\n":
                output = output + "            this.%s"%ctrlname + rtn
    return output
#指定されたコントロールのプロパティを生成、MakeCtrlPropsメソッドが利用するメソッド
#@numba.jit
def GetProp_CS(prop_kind, target):
    rtn = ""
    if prop_kind == "position":
        PosX = str(target["position"]["X"])
        PosY = str(target["position"]["Y"])
        rtn = ".Location = new System.Drawing.Point(%s,%s);" % (PosX, PosY)
    elif prop_kind == "text":
        text = str(target["text"])
        rtn = ".Text = \"%s\";" % text
    elif prop_kind == "":
        pass
    rtn += "\n"
    return rtn
#コントロールの宣言部分
#@numba.jit
def Defin_Ctrls_CS(ui_d):
    rtn = ""
    for ctrl_kind in ui_d:
        if ctrl_kind != "Window":
            for ctrl_name in ui_d[ctrl_kind]:
                ctrl_kind_t = Get_ctrl_kind_t_CS(ctrl_kind)
                rtn += "        private System.Windows.Forms.%s %s;\n"%(ctrl_kind_t,ctrl_name)
    return rtn

#JSONで管理している名前と違ってもいいようにここでC#での名前に変換する
#@numba.jit
def Get_ctrl_kind_t_CS(ctrl_kind):
    rtn = ""
    i = const.UIs.index(ctrl_kind)
    rtn = const.UIs_t_CS[i]
    return rtn
class Convert():
    def __init__(self, target_file, project_name):
        print("Converting "+target_file)
        self.starttime = time.time()
        f = open(const.project_dir + const.pathsep + target_file, 'r')
        self.ui_d = json.load(f)
        f.close()
        self.Convert_CS_WinForm(target_file, project_name)
    #  C#・WindowsForm向けのソースの生成メソッド
    def Convert_CS_WinForm(self, target_file, project_name):
        target_file = target_file.replace(".gson", "")
        target_window_name = target_file
        target_file = const.project_dir + const.pathsep + target_file + ".Designer.cs"
    
        wo = """namespace %s
{
    partial class %s
    {
        private void InitializeComponent()
        {
            \n""" % (project_name, target_window_name)

        for kind in const.UIs:
            if kind in self.ui_d:
                wo += MakeCtrlProps_CS(self.ui_d, kind)
        wo += "        }\n"
        wo += Defin_Ctrls_CS(self.ui_d)
        wo += """    }
}"""
        #ファイル書き込み
        sf = open(target_file, 'w')
        sf.write(wo)
        sf.close()
        self.endtime = time.time()
        print(self.endtime - self.starttime)
        print("Convert FINISHED!")