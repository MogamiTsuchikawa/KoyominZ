import UI_D,wx,os
proj_dir = ""
window_list = []
def Load_Proj(dirname):
    proj_dir = dirname

    
def Get_proj_dir():
    return proj_dir

class Manager_Window(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,title="KoyominZ Project Manager")
        self.SetSize(960,540)
        self.panel = wx.Panel(self,wx.ID_ANY)
        back_img_bm = wx.Image(os.path.dirname(__file__)+'/res/bg_KoyominZ.png').ConvertToBitmap()
        self.back_img = wx.StaticBitmap(self.panel,-1,back_img_bm,(0,0),self.GetClientSize())
        
        self.New_Btn = wx.Button(self.back_img,-1,label="New",pos=(655,120))
        self.New_Btn.SetSize(180,60)
        self.New_Btn.Bind(wx.EVT_BUTTON,self.New_Btn_Clicked)
        self.Load_Btn = wx.Button(self.back_img,-1,label="Load",pos=(580,190))
        self.Load_Btn.SetSize(180,60)
        self.Load_Btn.Bind(wx.EVT_BUTTON,self.Load_Btn_Clicked)
        self.Setting_Btn = wx.Button(self.back_img,-1,label="Setting",pos=(505,260))
        self.Setting_Btn.SetSize(180,60)
        self.Setting_Btn.Bind(wx.EVT_BUTTON,self.Setting_Btn_Clicked)
        self.OpenWebSite_Btn = wx.Button(self.back_img,-1,label="OpenWebSite",pos=(430,330))
        self.OpenWebSite_Btn.SetSize(180,60)
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
            if self.filename == "PROJECT.imp": #ファイル名に関しては後々再考
                Load_Proj(self.dirname)
    def Setting_Btn_Clicked(self,event):
        pass
    def OpenWebSite_Btn_Clicked(self,event):
        pass



class NewProject(wx.Frame):
    def __init__(self,parent):
        print("NewProject!")
        self.SetSize(960,540)
        self.panel = wx.Panel(self,wx.ID_ANY)
        MakeBtn = wx.Button(self.panel,-1,label="Make!",pos=(0,0))
app = wx.App(False)
frame = Manager_Window(None)
frame.Show()
app.MainLoop()