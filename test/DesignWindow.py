import wx,copy,json,numba
import const

class DesignWindow(wx.Frame):
    def __init__(self, parent, title):
        self.Move_Object = None
        self.Move_Object_Pos = None
        self.f = open("gui.json", 'r')
        self.ui_d = json.load(self.f)
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

        wx.Frame.__init__(self, parent, title=title)
        self.DW_panel = wx.Panel(self, wx.ID_ANY)
        self.Ctrls = {"Button": self.btn, "TextBox": self.textbox, "Label": self.label,"CheckBox": self.checkbox, "ComboBox": self.combobox, "ProgressBar": self.progressbar}
        self.Ctrls_Name = {"Button": self.btn_name, "TextBox": self.textbox_name, "Label": self.label_name,"CheckBox": self.checkbox_name, "ComboBox": self.combobox_name, "ProgressBar": self.progressbar_name}
        for Ctrl_t in self.Ctrls:
            self.Set_UI(Ctrl_t, self.Ctrls[Ctrl_t])

        self.DW_panel.Bind(wx.EVT_MOTION, self.OnMouseMove)
    def Set_UI(self,Target_UIkind, Target_UIs):
        i = 0
        for b in self.ui_d[Target_UIkind]:
            T_UI_b = self.ui_d[Target_UIkind][b]
            if Target_UIkind == "Button":
                Target_UIs.append(wx.Button(
                    self.DW_panel, -1,label=T_UI_b["text"], pos=(T_UI_b["positionX"], T_UI_b["positionY"])))
                self.btn_name.append(b)
            elif Target_UIkind == "TextBox":
                Target_UIs.append(wx.TextCtrl(
                    self.DW_panel, -1, pos=(T_UI_b["positionX"], T_UI_b["positionY"])))
                self.textbox_name.append(b)
            elif Target_UIkind == "Label":
                Target_UIs.append(wx.StaticText(
                    self.DW_panel, -1, label=T_UI_b["text"], pos=(T_UI_b["positionX"], T_UI_b["positionY"])))
                self.label_name.append(b)
            elif Target_UIkind == "CheckBox":
                Target_UIs.append(wx.CheckBox(
                    self.DW_panel, -1, label=T_UI_b["text"], pos=(T_UI_b["positionX"], T_UI_b["positionY"])))
                self.checkbox_name.append(b)
            elif Target_UIkind == "ComboBox":
                Target_UIs.append(wx.ComboBox(
                    self.DW_panel, -1, pos=(T_UI_b["positionX"], T_UI_b["positionY"])))
                self.combobox_name.append(b)
            elif Target_UIkind == "ProgressBar":
                Target_UIs.append(
                    wx.Gauge(self.DW_panel, -1, pos=(T_UI_b["positionX"], T_UI_b["positionY"])))
                self.progressbar_name.append(b)
            Target_UIs[i].Bind(wx.EVT_LEFT_DOWN, self.Left_Down)
            Target_UIs[i].Bind(wx.EVT_RIGHT_DOWN, self.Right_Down)
            i += 1

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
                    self.ui_d[ctrl_kind][ctrl_name]["positionX"] = self.Move_Object_Pos[0]
                    self.ui_d[ctrl_kind][ctrl_name]["positionY"] = self.Move_Object_Pos[1]
                    t_index = -1
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
        elif Change_Kind == "positionX":
            point = target_UI_o.GetPosition()
            target_UI_o.SetPosition(wx.Point(float(Change_Value),point[1]))
            print(str(target_UI_o.GetPosition()))
        elif Change_Kind == "positionY":
            point = target_UI_o.GetPosition()
            target_UI_o.SetPosition(wx.Point(point[0],float(Change_Value)))

    
    def Save(self):

        f = open("gui.json",'w')
        json.dump(self.ui_d,f,indent=4)
        f.close()