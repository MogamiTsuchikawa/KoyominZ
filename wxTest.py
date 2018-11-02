import wx,wx.grid

class Main(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        panel = wx.Panel(self, wx.ID_ANY)
        #textbox = wx.TextCtrl(panel,-1)
        #textbox.SetBackgroundColour("white")
        label = wx.StaticText(panel,-1,"TEST",pos=(0,20))
        checkbox = wx.CheckBox(panel,-1,"TEST",pos=(0,40))
        btn= wx.Button(panel,-1)
        btn.Label = "hello"
        t_grid = wx.grid.Grid(self)
        t_grid.Size = (200,200)
        t_grid.CreateGrid(1,1)
        t_grid.AppendRows(2)
app = wx.App(False)
frame = Main(None, "MouseEvents")
frame.Show()

app.MainLoop()