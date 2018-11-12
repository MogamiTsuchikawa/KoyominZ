import wx
import copy
import json


class DesignWindow(wx.Frame):
    def __init__(self, parent, title):
        self.Move_Object = None
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
        Ctrls = {"Button": self.btn, "TextBox": self.textbox, "Label": self.label,
                 "CheckBox": self.checkbox, "ComboBox": self.combobox, "ProgressBar": self.progressbar}
        for Ctrl_t in Ctrls:
            self.Set_UI(Ctrl_t, Ctrls[Ctrl_t])

        self.DW_panel.Bind(wx.EVT_MOTION, self.OnMouseMove)
        # btn[0].Bind(wx.EVT_BUTTON,self.btn_Clicked)

    def Set_UI(self,Target_UIkind, Target_UIs):
        i = 0
        for b in self.ui_d[Target_UIkind]:
            T_UI_b = self.ui_d[Target_UIkind][b]
            if Target_UIkind == "Button":
                Target_UIs.append(wx.Button(
                    self.DW_panel, -1, label=T_UI_b["text"], pos=(T_UI_b["positionX"], T_UI_b["positionY"])))
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
            self.Move_Object = None
            # Show_StBar()

    def Right_Down(self, event):
        Clicked_Object = event.GetEventObject()

    def OnMouseMove(self, event):

        pos = event.GetPosition()
        self.SetTitle('OnMouseMove' + str(pos))

        if self.Move_Object is not None:
            # print(Move_Object)
            self.Move_Object.SetPosition(pos)

    def ChangeCtrlValue(self, Target_UI_kind, Target_UI_name, Change_Kind, Change_Value):
        if Target_UI_kind == "Button":
            index = self.btn_name.index(Target_UI_name)
            target_UI_o = self.btn[index]
            if Change_Kind == "text":
                target_UI_o.Label = Change_Value
                print(Change_Value)
                print(target_UI_o)
