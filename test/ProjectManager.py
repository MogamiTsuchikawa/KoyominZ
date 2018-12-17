import UI_D,wx
def Load_Proj():
    Proj_Direc = ""
    

class Manager_Window(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,title="KoyominZ Project Manager")
        self.SetSize(960,540)
        self.panel = wx.Panel(self,wx.ID_ANY)
        self.New_Btn = wx.Button(self.panel,-1,label="New",pos=(10,10))
        self.New_Btn.Bind(wx.EVT_BUTTON,self.New_Btn_Clicked)
        self.Load_Btn = wx.Button(self.panel,-1,label="Load",pos=(10,40))
        self.Load_Btn.Bind(wx.EVT_BUTTON,self.Load_Btn_Clicked)
        self.Setting_Btn = wx.Button(self.panel,-1,label="Setting",pos=(10,70))
        self.Setting_Btn.Bind(wx.EVT_BUTTON,self.Setting_Btn_Clicked)
        self.OpenWebSite_Btn = wx.Button(self.panel,-1,label="New",pos=(10,100))
        self.OpenWebSite_Btn.Bind(wx.EVT_BUTTON,self.OpenWebSite_Btn_Clicked)
    def New_Btn_Clicked(self,event):
        pass
    def Load_Btn_Clicked(self,event):
        self.dirname = ""
        fo_dialog = wx.FileDialog(self, "ファイルを選択してください", self.dirname, "", "*.*", wx.FD_OPEN)
        if fo_dialog.ShowModal() == wx.ID_OK:
            self.filename = fo_dialog.GetFilename()
            self.dirname = fo_dialog.GetDirectory()
            print(self.filename)
            print(self.dirname)
    def Setting_Btn_Clicked(self,event):
        pass
    def OpenWebSite_Btn_Clicked(self,event):
        pass

def Load_Proj_XML():
    pass
    #projectの含んでいるファイルやターゲット環境などのビルドに必要な情報を格納

app = wx.App(False)
frame = Manager_Window(None)
frame.Show()
app.MainLoop()