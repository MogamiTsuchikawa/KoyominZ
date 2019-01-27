import UI_D,wx,os,const,json

class NewProject(wx.Frame):
    def __init__(self,parent):
        print("NewProject!")
        wx.Frame.__init__(self,parent,title="KoyominZ [New Project]")
        self.SetSize(960,540)
        self.panel = wx.Panel(self,wx.ID_ANY)
        self.MakeProjBtn = wx.Button(self.panel,-1,label="Make!",pos=(800,450))
        self.MakeProjBtn.Bind(wx.EVT_BUTTON,self.MakeProjBtn_Clicked)
        self.ProjNameTextbox = wx.TextCtrl(self.panel,-1,pos=(100,100),style=wx.TE_MULTILINE)
        self.ProjPathTextbox = wx.TextCtrl(self.panel,-1,pos=(100,200),style=wx.TE_MULTILINE)
        self.ProjNameTextbox.SetValue("sample")
    def MakeProjBtn_Clicked(self,event):
        proj_name = self.ProjNameTextbox.GetValue()
        print(type(proj_name))
        if self.ProjNameTextbox.GetValue != "":
            #Pathはあとでやる
            f_path = str(os.path.dirname(__file__))
            self.MakeNewProject(f_path,proj_name)
        
    def MakeNewProject(self,f_path,name):
        proj_path = f_path +const.pathsep + "projects"+ const.pathsep + name
        print(proj_path)
        os.makedirs(proj_path)
        
        imp_d = {}
        imp_d["aboutthis"] = {"name" : name , "kind" : "dotnetcore_winform"}
        imp_d["sourcefiles"] = {"cs" : "Program,Form1","gson":"Form1"}
        imp_f = open(proj_path + os.pathsep + "PROJECT.imp",'w')
        json.dump(imp_d,imp_f,indent=4)
        imp_f.close()
        Form1_f = open(proj_path + os.pathsep + "Form1.gson",'w')
        Form1_d = UI_D.Make_ui_d("Form1")
        json.dump(Form1_d,Form1_f,indent=4)
        Form1_f.close()
        const.project_dir = proj_path
        const.project_name = name
        const.project_kind = "dotnetcore_winform"
        os.system("cd "+proj_path)
        os.system("dotnet new winform -o "+name)
        self.Close(True)
        wx.Exit()


