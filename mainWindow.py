import wx,json,copy,asyncio,threading
import DesignWindow
StaBar = None    
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        def Change_StaBar():
            mv_obj = DesignWindow.Move_Object
            if mv_obj is not None:
                self.SetStatusText("Yes")
            else:
                self.SetStatusText("Nooooo")
            t = threading.Timer(0.1,Change_StaBar)
            t.start()
        wx.Frame.__init__(self, parent, title=title)
        panel = wx.Panel(self,wx.ID_ANY)
        StaBar = self.CreateStatusBar()
        Sub_Window = DesignWindow.DesignWindow(self,"MousePoint")
        Sub_Window_ID = Sub_Window.Show()
        t = threading.Thread(target=Change_StaBar)
        t.start()
        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(asyncio.gather(Change_StaBar(self)))

app = wx.App(False)
frame = MainWindow(None, "MouseEvents")
frame.Show()

app.MainLoop()