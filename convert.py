import wx
import json
import numba
import xmltodict
import xml.etree.ElementTree as ET

def MakeCtrlProps(ui_d, kind):
    output = ""
    ui_d_a = ui_d[kind]
    for ctrlname in ui_d_a:
        target = ui_d_a[ctrlname]
        output += "            this.%s.Name = \"%s\"\n" % (
            ctrlname, ctrlname)
        for prop_kind in target:
            rtn = GetProp(prop_kind, target)
            if rtn != "\n":
                output = output + "            this.%s"%ctrlname + GetProp(prop_kind, target)
        return output

def GetProp(prop_kind, target):
    rtn = ""
    if prop_kind == "positionX":
        PosX = str(target["positionX"])
        PosY = str(target["positionY"])
        rtn = ".Location = new System.Drawing.Point(%s,%s);" % (PosX, PosY)
    elif prop_kind == "text":
        text = str(target["text"])
        rtn = ".Text = \"%s\"" % text
    elif prop_kind == "":
        pass
    rtn += "\n"
    return rtn

class Convert():
    def __init__(self, target_file, project_name):
        print("Converting "+target_file)
        self.target_file = target_file
        f = open(self.target_file, 'r')
        self.ui_d = json.load(f)
        f.close()
        self.Convert_CS_WinForm(target_file, project_name)

    def Convert_CS_WinForm(self, target_file, project_name):
        target_file = target_file.replace(".json", "")
        target_window_name = target_file
        target_file = target_file + ".Designer.cs"

        wo = """namespace %s
{
    partial class %s
    {
        private void InitializeComponent()
        {
            \n""" % (project_name, target_window_name)

        UIs = {"Button", "TextBox", "Label",
               "CheckBox", "ComboBox", "ProgressBar"}
        for kind in UIs:
            wo += MakeCtrlProps(self.ui_d, kind)
        sf = open(target_file, 'w')
        sf.write(wo)
        sf.close()
        print("Convert FINISHED!")
