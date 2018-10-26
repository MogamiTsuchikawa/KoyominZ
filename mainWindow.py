import wx,json,copy,asyncio,threading
import DesignWindow
StaBar = None

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.window_list = ["gui"]
        
        wx.Frame.__init__(self, parent, title=title)
        self.SetSize(500,600)
        panel = wx.Panel(self,wx.ID_ANY)
        
        StaBar = self.CreateStatusBar()
        self.Sub_Window = DesignWindow.DesignWindow(self,"MousePoint")
        Sub_Window_ID = self.Sub_Window.Show()
        btn = wx.Button(panel,-1)
        btn.Bind(wx.EVT_LEFT_DOWN,self.btn_click)
        self.CtrlList = wx.TreeCtrl(panel,-1,pos=(20,20))
        self.CtrlList.Size = (200,200)
        self.SetCtrlList(self.CtrlList)
    def btn_click(self,i):
        self.Sub_Window.ChangeCtrlValue("Button","btn1","text","Clicked")
    def SetCtrlList(self,ctrllist):
        self.cl_root = ctrllist.AddRoot("Windows")
        self.cl_d = []
        self.cl_names = []
        i = 0
        win_i = 0
        for win_name in self.window_list:
            
            self.cl_d.append(ctrllist.AppendItem(self.cl_root,win_name))
            self.cl_names.append({win_name,"Window",win_name})
            win_i = i
            i+=1
            f = open(win_name+".json")
            ui_d = json.load(f)
            UIs = {"Button","TextBox","Label","CheckBox","ComboBox","ProgressBar"}
            ctrl_i=0
            for ui in UIs:
                self.cl_d.append(ctrllist.AppendItem(self.cl_d[win_i],ui))
                self.cl_names.append({ui+".root","root"})
                ctrl_i = i
                i+=1
                
                for ctrl_name in ui_d[ui]:
                    self.cl_d.append(ctrllist.AppendItem(self.cl_d[ctrl_i],ctrl_name))
                    self.cl_names.append({win_name,ui,ctrl_name})
                    i+=1
                
app = wx.App(False)
frame = MainWindow(None, "MouseEvents")
frame.Show()

app.MainLoop()