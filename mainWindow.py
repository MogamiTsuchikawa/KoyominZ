import wx
btn_Move = False
btn =[]
class myFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        panel = wx.Panel(self, wx.ID_ANY)
        btn.append(wx.Button(panel, -1, label="Btn", pos=(10, 10)))

        panel.Bind(wx.EVT_MOTION,self.OnMouseMove) 
        btn[0].Bind(wx.EVT_BUTTON,self.btn_Clicked)
    def OnMouseMove(self, event):
        global btn_Move
        pos = event.GetPosition()
        self.SetTitle( 'OnMouseMove' + str(pos))
        if btn_Move:
            btn[0].SetPosition(pos)
    
    def btn_Clicked(self,event):
        global btn_Move
        if btn_Move:
            btn_Move = False
            print(btn_Move)
        else:
            btn_Move = True
            print(btn_Move)
    
app = wx.App(False)
frame = myFrame(None, "MouseEvents")
frame.Show()
app.MainLoop()