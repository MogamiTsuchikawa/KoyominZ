import wx,copy,json
Move_Object = None
f = open("gui.json",'r')
ui_d = json.load(f)
DW_panel = None
btn =[]
textbox = []
label = []
checkbox = []

class DesignWindow(wx.Frame):
    def __init__(self, parent, title):
        def Set_UI(Target_UIkind,Target_UIs):
            i = 0
            for b in ui_d[Target_UIkind]:
                T_UI_b = ui_d[Target_UIkind][b]
                if Target_UIkind == "Button":
                    Target_UIs.append(wx.Button(DW_panel,-1,label=T_UI_b["text"],pos=(T_UI_b["positionX"],T_UI_b["positionY"])))
                elif Target_UIkind == "TextBox":
                    Target_UIs.append(wx.TextCtrl(DW_panel,-1,pos=(T_UI_b["positionX"],T_UI_b["positionY"])))
                elif Target_UIkind == "Label":
                    Target_UIs.append(wx.StaticText(DW_panel,-1,label=T_UI_b["text"],pos=(T_UI_b["positionX"],T_UI_b["positionY"])))
                elif Target_UIkind == "CheckBox":
                    Target_UIs.append(wx.CheckBox(DW_panel,-1,label=T_UI_b["text"],pos=(T_UI_b["positionX"],T_UI_b["positionY"])))
                Target_UIs[i].Bind(wx.EVT_LEFT_DOWN,self.Left_Down)
                Target_UIs[i].Bind(wx.EVT_RIGHT_DOWN,self.Right_Down)
                i+=1
            
        wx.Frame.__init__(self, parent, title=title)
        DW_panel = wx.Panel(self, wx.ID_ANY)
        Ctrls = {"Button":btn,"TextBox":textbox,"Label":label,"CheckBox":checkbox}
        for Ctrl_t in Ctrls:
            Set_UI(Ctrl_t,Ctrls[Ctrl_t])
        
        
        DW_panel.Bind(wx.EVT_MOTION,self.OnMouseMove) 
        #btn[0].Bind(wx.EVT_BUTTON,self.btn_Clicked)
    
    def Left_Down(self,event):
        
        global DW_panel
        global Move_Object
        Clicked_Object = event.GetEventObject()
        #print(Clicked_Object)
        if Move_Object is None:
            Move_Object = Clicked_Object
            #SetStatusText("移動中")
        elif Move_Object == Clicked_Object:
            Move_Object = None
            #Show_StBar()
            

    def Right_Down(self,event):
        Clicked_Object = event.GetEventObject()

    def OnMouseMove(self, event):
        global Move_Object
        pos = event.GetPosition()
        self.SetTitle( 'OnMouseMove' + str(pos))
        
        if Move_Object is not None:
            #print(Move_Object)
            Move_Object.SetPosition(pos)
    