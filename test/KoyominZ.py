import ProjectManager,Main,const #source
import wx,platform
#ProjectManager.Manager_Windowを表示
const.os = platform.system()
if const.os == "Windows":
    const.pathsep = "\\"
proj_m = wx.App(False)
proj_m_f = ProjectManager.Manager_Window(None)
proj_m_f.Show()
proj_m.MainLoop()
#ProjectManager.Manager_Windowを表示後に取得
if const.project_dir == "":
    pass
else:
    #MainWin = wx.App(False)
    MainWin_f = Main.MainWindow(None,const.project_name,False)
    MainWin_f.Show()
    MainWin.MainLoop()
    