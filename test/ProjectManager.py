import UI_D,wx,os,const,json,NewProject
proj_dir = ""
window_list = []

    
def Get_proj_dir():
    return proj_dir

class Manager_Window(wx.Frame):
    def __init__(self,parent):
        self.MoveOrder = []
        wx.Frame.__init__(self,parent,title="KoyominZ Project Manager")
        self.parent = parent
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
        NewProject_o = wx.App(False)
        NewProject_f = NewProject.NewProject(self)
        NewProject_f.Show()
        NewProject_o.MainLoop()
        print("Close")
        self.Close(True)
    def Load_Btn_Clicked(self,event):
        self.dirname = ""
        fo_dialog = wx.FileDialog(self, "ファイルを選択してください", self.dirname, "", "*.*", wx.FD_OPEN)
        if fo_dialog.ShowModal() == wx.ID_OK:
            self.filename = fo_dialog.GetFilename()
            self.dirname = fo_dialog.GetDirectory()
            print(self.filename)
            print(self.dirname)
            if self.filename == "PROJECT.imp": #ファイル名に関しては後々再考
                self.Load_Proj(self.dirname)
                self.Close(True)
    def Setting_Btn_Clicked(self,event):
        pass
    def OpenWebSite_Btn_Clicked(self,event):
        pass
    def Load_Proj(self,dirname):
        proj_dir = dirname
        # PROJECT.imp のパージ＆constへ値入力
        pf = open(proj_dir + '/PROJECT.imp','r')
        p_info = json.load(pf)
        const.project_dir = proj_dir
        const.project_name = p_info['aboutthis']['name']
        const.project_kind = p_info['aboutthis']['kind']
        #ソースファイル extは拡張子キーを入れる
        for ext in  p_info['sourcefiles']:
            const.source_files[ext] = p_info['sourcefiles'][ext].split(",")
    def MoveCtrl(self,event):
        for i in range(len(self.MoveOrder)):
            order_d = self.MoveOrder[i]
            x_v = order_d["new_point"][0] - order_d["old_point"][0]
            y_v = order_d["new_point"][1] - order_d["old_point"][1]
            m_t = order_d["time"] / 2
            target_obj = order_d["obj"]
            pos = target_obj.GetPosition()
            if x_v != 0:
                m_x = x_v / m_t
                pos = wx.Point(pos[0]+m_x,pos[1])
                target_obj.SetPosition()
            if y_v != 0:
                m_y = y_v / m_t
                pos = wx.Point(pos[0],pos[1]+m_y)
                target_obj.SetPosition()
    def SetMoveOrder(self,target_obj,target_point,time):
        target_current_ponit = target_obj.GetPosition()
        order_d = {"obj":target_obj,"new_point":target_point,"old_point":target_current_ponit,"time":time}
        self.MoveOrder.append(order_d)
