import Main,ProjectManager,const #source
import wx
#ProjectManager.Manager_Windowを表示
proj_m = wx.App(False)
proj_m_f = ProjectManager.Manager_Window(None)
proj_m_f.Show()
#proj_m.MainLoop()
#ProjectManager.Manager_Windowを表示後に取得
if const.project_dir == "":
    wx.Exit()
else:
    #MainWin = wx.App(False)
    #MainWin_f = Main.MainWindow(None)
    #MainWin_f.Show()
    #MainWin.MainLoop()
    pass
