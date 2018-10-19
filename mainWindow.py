import wx,json,copy
btn_Move = False
Move_Object = None
f = open("gui.json",'r')
ui_d = json.load(f)
DW_panel = None
btn =[]
class DesignWindow(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        DW_panel = wx.Panel(self, wx.ID_ANY)
        i = 0
        for b in ui_d["Button"]:
            print(ui_d["Button"][b])
            btn_b = ui_d["Button"][b]
            btn.append(wx.Button(DW_panel,-1,label=btn_b["text"],pos=(btn_b["positionX"],btn_b["positionY"])))
            btn[i].Bind(wx.EVT_LEFT_DOWN,self.Left_Down)
            btn[i].Bind(wx.EVT_RIGHT_DOWN,self.Right_Down)
            i+=1
        
        DW_panel.Bind(wx.EVT_MOTION,self.OnMouseMove) 
        #btn[0].Bind(wx.EVT_BUTTON,self.btn_Clicked)
    
    def Left_Down(self,event):
        global DW_panel
        global Move_Object
        Clicked_Object = event.GetEventObject()
        #print(Clicked_Object)
        if Move_Object is None:
            Move_Object = Clicked_Object
        elif Move_Object == Clicked_Object:
            Move_Object = None
            

    def Right_Down(self,event):
        Clicked_Object = event.GetEventObject()

    def OnMouseMove(self, event):
        global Move_Object
        pos = event.GetPosition()
        self.SetTitle( 'OnMouseMove' + str(pos))
        
        if Move_Object is not None:
            print(Move_Object)
            Move_Object.SetPosition(pos)
    
    def btn_Clicked(self,event):
        global btn_Move
        if btn_Move:
            btn_Move = False
            print(btn_Move)
        else:
            btn_Move = True
            print(btn_Move)
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)

        Sub_Window = DesignWindow(self,"MousePoint")
        Sub_Window_ID = Sub_Window.Show()
app = wx.App(False)
frame = MainWindow(None, "MouseEvents")
frame.Show()

app.MainLoop()