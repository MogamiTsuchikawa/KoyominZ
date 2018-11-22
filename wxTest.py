import wx,wx.grid
import convert

class Main(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        panel = wx.Panel(self, wx.ID_ANY)
        menu_bar_items = []
        menu_bar = wx.MenuBar()
        menu_bar_file = wx.Menu()
        menu_bar_items_i = 0
        for m_text in {"NewFile","OpenFile"}:
            menu_bar_items.append(wx.MenuItem(menu_bar_file,wx.ID_NEW,text=m_text,kind=wx.ITEM_NORMAL))
            menu_bar_items[menu_bar_items_i].SetBitmap(wx.Bitmap("res/icon/"+m_text+".png"))
            menu_bar_file.Append(menu_bar_items[menu_bar_items_i])
            menu_bar_items_i += 1
        
        menu_bar_edit = wx.Menu()
        for m_text in {"Cut","Copy","Paste"}:
            menu_bar_items.append(wx.MenuItem(menu_bar_file,wx.ID_NEW,text=m_text,kind=wx.ITEM_NORMAL))
            menu_bar_items[menu_bar_items_i].SetBitmap(wx.Bitmap("res/icon/"+m_text+".png"))
            menu_bar_edit.Append(menu_bar_items[menu_bar_items_i])
            menu_bar_items_i += 1
        menu_bar.Append(menu_bar_file,"File")
        menu_bar.Append(menu_bar_edit,"Edit")
        self.SetMenuBar(menu_bar)
        self.Show()

app = wx.App(False)
frame = Main(None, "MouseEvents")
frame.Show()

conv = convert.Convert("gui.json","TEST")



app.MainLoop()