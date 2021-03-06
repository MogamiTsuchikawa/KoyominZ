import wx,copy,json
import const,UI_D
import format_check

class Design_Window(wx.Frame):
    def __init__(self, parent, winname):
        self.winname = winname
        self.Move_Object = None
        self.Move_Object_Pos = None
        self.f = open(const.project_dir+const.pathsep+winname+".gson", 'r')
        self.ui_d = UI_D.ui_d_s[winname]
        self.DW_panel = None
        self.btn = []
        self.btn_name = []
        self.textbox = []
        self.textbox_name = []
        self.label = []
        self.label_name = []
        self.checkbox = []
        self.checkbox_name = []
        self.combobox = []
        self.combobox_name = []
        self.progressbar = []
        self.progressbar_name = []

        wx.Frame.__init__(self, parent)
        self.DW_panel = wx.Panel(self, wx.ID_ANY)
        self.Ctrls = {"Button": self.btn, "TextBox": self.textbox, "Label": self.label,"CheckBox": self.checkbox, "ComboBox": self.combobox, "ProgressBar": self.progressbar}
        self.Ctrls_Name = {"Button": self.btn_name, "TextBox": self.textbox_name, "Label": self.label_name,"CheckBox": self.checkbox_name, "ComboBox": self.combobox_name, "ProgressBar": self.progressbar_name}
        for Ctrl_t in self.Ctrls:
            if Ctrl_t in self.ui_d:
                
                self.Set_UI(Ctrl_t, self.Ctrls[Ctrl_t])
        # Windowの設定
        if "size" in self.ui_d["Window"]:
            self.SetSize(self.ui_d["Window"]["size"]["X"],self.ui_d["Window"]["size"]["Y"])
        if "text" in self.ui_d["Window"]:
            self.SetTitle(self.ui_d["Window"]["text"])
        self.DW_panel.Bind(wx.EVT_MOTION, self.OnMouseMove)
    def Set_Ctrl(self,Target_Ctrl_kind,Target_Ctrl_name,mode,Target_Ctrl_obj):
        ui_d_c = {}
        if mode == "ADD":
            i = 1
            while i != -1:
                new_name = Target_Ctrl_kind + str(i)
                if new_name in self.ui_d[Target_Ctrl_kind]:
                    Target_Ctrl_name = new_name
                    i = -1
                else:
                    i += 1
            if Target_Ctrl_kind == "Button" or Target_Ctrl_kind == "Label" or Target_Ctrl_kind == "CheckBox":
                ui_d_c[Target_Ctrl_name] = {"position":{"X":10,"Y":10},"text":Target_Ctrl_name}
            #他のコントロール分も後で書く
        else:
            ui_d_c = self.ui_d[Target_Ctrl_kind]

        #コントロール追加部分
        for name in ui_d_c:
            ui_dcd = ui_d_c[name]
            if Target_Ctrl_kind == "Button":
                Target_Ctrl_obj.append(wx.Button(
                    self.DW_panel, -1,label=ui_dcd["text"], pos=(ui_dcd["position"]["X"], ui_dcd["position"]["Y"])))
                self.btn_name.append(name)
            elif Target_Ctrl_kind == "TextBox":
                Target_Ctrl_obj.append(wx.TextCtrl(
                    self.DW_panel, -1, pos=(ui_dcd["position"]["X"], ui_dcd["position"]["Y"])))
                self.textbox_name.append(name)
            elif Target_Ctrl_kind == "Label":
                Target_Ctrl_obj.append(wx.StaticText(
                    self.DW_panel, -1,label=ui_dcd["text"], pos=(ui_dcd["position"]["X"], ui_dcd["position"]["Y"])))
                self.label_name.append(name)
            elif Target_Ctrl_kind == "CheckBox":
                Target_Ctrl_obj.append(wx.CheckBox(
                    self.DW_panel, -1,label=ui_dcd["text"], pos=(ui_dcd["position"]["X"], ui_dcd["position"]["Y"])))
                self.checkbox_name.append(name)
            elif Target_Ctrl_kind == "ComboBox":
                Target_Ctrl_obj.append(wx.ComboBox(
                    self.DW_panel, -1, pos=(ui_dcd["position"]["X"], ui_dcd["position"]["Y"])))
                self.combobox_name.append(name)
            elif Target_Ctrl_kind == "ProgressBar":
                Target_Ctrl_obj.append(wx.Gauge(
                    self.DW_panel, -1, pos=(ui_dcd["position"]["X"], ui_dcd["position"]["Y"])))
                self.progressbar_name.append(name)
            


    def Set_UI(self,Target_UIkind, Target_UIs):
        #
        #      削除予定
        #   Set_Ctrlメソッド完成時にSet_UIは初期化時にSet_Ctrlへ渡す用のメソッドに変更。
        #
        i = 0
        for b in self.ui_d[Target_UIkind]:
            T_UI_b = self.ui_d[Target_UIkind][b]
            if Target_UIkind == "Button":
                Target_UIs.append(wx.Button(
                    self.DW_panel, -1,label=T_UI_b["text"], pos=(T_UI_b["position"]["X"], T_UI_b["position"]["Y"])))
                self.btn_name.append(b)
            elif Target_UIkind == "TextBox":
                Target_UIs.append(wx.TextCtrl(
                    self.DW_panel, -1, pos=(T_UI_b["position"]["X"], T_UI_b["position"]["Y"])))
                self.textbox_name.append(b)
            elif Target_UIkind == "Label":
                Target_UIs.append(wx.StaticText(
                    self.DW_panel, -1, label=T_UI_b["text"], pos=(T_UI_b["position"]["X"], T_UI_b["position"]["Y"])))
                self.label_name.append(b)
            elif Target_UIkind == "CheckBox":
                Target_UIs.append(wx.CheckBox(
                    self.DW_panel, -1, label=T_UI_b["text"], pos=(T_UI_b["position"]["X"], T_UI_b["position"]["Y"])))
                self.checkbox_name.append(b)
            elif Target_UIkind == "ComboBox":
                Target_UIs.append(wx.ComboBox(
                    self.DW_panel, -1, pos=(T_UI_b["position"]["X"], T_UI_b["position"]["Y"])))
                self.combobox_name.append(b)
            elif Target_UIkind == "ProgressBar":
                Target_UIs.append(
                    wx.Gauge(self.DW_panel, -1, pos=(T_UI_b["position"]["X"], T_UI_b["position"]["Y"])))
                self.progressbar_name.append(b)
            Target_UIs[i].Bind(wx.EVT_LEFT_DOWN, self.Left_Down)
            Target_UIs[i].Bind(wx.EVT_RIGHT_DOWN, self.Right_Down)
            if("sizeX" in T_UI_b):
                Target_UIs[i].SetSize(float(T_UI_b["sizeX"]),float(T_UI_b["sizeY"]))
            i += 1
        #
        #     ここまで
        #
    def Left_Down(self, event):

        Clicked_Object = event.GetEventObject()
        
        # print(Clicked_Object)
        if self.Move_Object is None:
            self.Move_Object = Clicked_Object
            # SetStatusText("移動中")
        elif self.Move_Object == Clicked_Object:
            ctrl_name =""
            t_index = -1
            for ctrl_kind in const.UIs:
                ctrls = self.Ctrls[ctrl_kind]
                for index in range(len(ctrls)):
                    if Clicked_Object == ctrls[index]:
                        t_index = index
                if t_index != -1:
                    ctrls_name_object = self.Ctrls_Name[ctrl_kind]
                    ctrl_name = ctrls_name_object[t_index]
                    print(ctrl_name)
                    self.ui_d[ctrl_kind][ctrl_name]["position"]["X"] = self.Move_Object_Pos[0]
                    self.ui_d[ctrl_kind][ctrl_name]["position"]["Y"] = self.Move_Object_Pos[1]
                    t_index = -1
                    const.update_main_window_showdata =True #MainWindowのプロパティ表示を更新
            self.Move_Object = None

    def Right_Down(self, event):
        Clicked_Object = event.GetEventObject()

    def OnMouseMove(self, event):
        pos = event.GetPosition()
        self.SetTitle('OnMouseMove' + str(pos))
        if self.Move_Object is not None:
            self.Move_Object.SetPosition(pos)
            self.Move_Object_Pos = pos
            
    def ChangeCtrlValue(self, Target_UI_kind, Target_UI_name, Change_Kind, Change_Value):
        index = self.Ctrls_Name[Target_UI_kind].index(Target_UI_name)
        target_UI_o = self.Ctrls[Target_UI_kind][index]
        if Change_Kind == "text":
            target_UI_o.Label = Change_Value
            print(Change_Value)
            print(target_UI_o)
        #positionX,Yの代わり。','によって区切り
        elif Change_Kind == "position":
            rtn = format_check.format_check(Target_UI_kind,Change_Kind,Change_Value)
            if rtn == "OK":
                c_point_s = Change_Value.split(",")
                c_point = wx.Point(float(c_point_s[0]),float(c_point_s[1]))
                target_UI_o.SetPosition(c_point)
            else:
                return rtn
        #sizeX,Yの代わり
        elif Change_Kind == "size":
            rtn = format_check.format_check(Target_UI_kind,Change_Kind,Change_Value)
            if rtn =="OK":
                c_size_s = Change_Value.split(",")
                target_UI_o.SetSize(float(c_size_s[0]),float(c_size_s[1]))
            else:
                return rtn
        elif Change_Kind == "background_color":
            rtn = format_check.format_check(Target_UI_kind,Change_Kind,Change_Value)
            if rtn == "OK":
                color_d = Change_Value.split(",")# sys_color,Blue  や RGB,R値,B値,G値　のように来る
                if color_d[0] == "sys_color":
                    target_UI_o.SetBackgroundColour(color_d[1])
                if color_d[0] == "RGB":
                    target_UI_o.SetBackgroundColour(wx.Colour(int(color_d[1]),int(color_d[2]),int(color_d[3])))
        elif Change_Kind == "foreround_color":
            rtn = format_check.format_check(Target_UI_kind,Change_Kind,Change_Value)
            if rtn == "OK":
                color_d = Change_Value.split(",")# sys_color,Blue  や RGB,R値,B値,G値　のように来る
                if color_d[0] == "sys_color":
                    target_UI_o.SetForegroundColour(color_d[1])
                if color_d[0] == "RGB":
                    target_UI_o.SetForegroundColour(wx.Colour(int(color_d[1]),int(color_d[2]),int(color_d[3])))


    def Add_Ctrl(self,ctrl_kind):
        self.Set_UI(ctrl_kind, self.Ctrls[ctrl_kind])
    # 使うかよくワカランのでコメントアウト
    #def Save(self):
    #    f = open(const.project_dir+const.pathsep+self.winname+".gson",'w')
    #    json.dump(self.ui_d,f,indent=4)
    #    f.close()