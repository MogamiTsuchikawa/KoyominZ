import wx,json,copy,asyncio,threading,wx.grid
import DesignWindow
StaBar = None

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.window_list = ["gui"]
        wx.Frame.__init__(self, parent, title=title)
        self.SetSize(500, 600)
        panel = wx.Panel(self, wx.ID_ANY)
        #
        menu_bar_items = []
        menu_bar = wx.MenuBar()
        self.menu_bar_file = wx.Menu()
        menu_bar_items_i = 0
        for m_text in {"NewFile","OpenFile"}:
            menu_bar_items.append(wx.MenuItem(self.menu_bar_file,wx.ID_NEW,text=m_text,kind=wx.ITEM_NORMAL))
            menu_bar_items[menu_bar_items_i].SetBitmap(wx.Bitmap("res/icon/"+m_text+".png"))
            self.menu_bar_file.Append(menu_bar_items[menu_bar_items_i])
            menu_bar_items_i += 1
        
        self.menu_bar_edit = wx.Menu()
        for m_text in {"Cut","Copy","Paste"}:
            menu_bar_items.append(wx.MenuItem(self.menu_bar_file,wx.ID_NEW,text=m_text,kind=wx.ITEM_NORMAL))
            menu_bar_items[menu_bar_items_i].SetBitmap(wx.Bitmap("res/icon/"+m_text+".png"))
            self.menu_bar_edit.Append(menu_bar_items[menu_bar_items_i])
            menu_bar_items_i += 1
        menu_bar.Append(self.menu_bar_file,"File")
        menu_bar.Append(self.menu_bar_edit,"Edit")
        self.SetMenuBar(menu_bar)

        #self.Show(True)
        #
        StaBar = self.CreateStatusBar()
        self.Sub_Window = DesignWindow.DesignWindow(self, "MousePoint")
        Sub_Window_ID = self.Sub_Window.Show()
        btn = wx.Button(panel, -1,pos=(50,600))
        btn.Bind(wx.EVT_LEFT_DOWN, self.btn_click)
        self.CtrlList = wx.TreeCtrl(panel, -1, pos=(0, 20))
        self.CtrlList.Size = (200, 400)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,self.CtrlList_Clicked, self.CtrlList)
        self.SetCtrlList(self.CtrlList)
        self.CtrlInfoGrid = wx.grid.Grid(self)
        self.CtrlInfoGrid.CreateGrid(1, 1)
        self.CtrlInfoGrid.Position = (210, 20)
        self.CtrlInfoGrid.Size = (200, 400)
        #self.CtrlInfoGrid.Bind(wx.grid.EVT_GRID_CMD_CELL_LEFT_CLICK,self.CtrlInfoGrid_Clicked())

    def btn_click(self, i):
        self.Sub_Window.ChangeCtrlValue("Button", "btn1", "text", "Clicked")

    def SetCtrlList(self, ctrllist):
        self.cl_root = ctrllist.AddRoot("Windows")
        self.cl_d = []
        self.cl_names = []
        i = 0
        win_i = 0
        for win_name in self.window_list:

            self.cl_d.append(ctrllist.AppendItem(self.cl_root, win_name))
            self.cl_names.append({win_name, "Window", win_name})
            win_i = i
            i += 1
            f = open(win_name+".json")
            ui_d = json.load(f)
            UIs = {"Button", "TextBox", "Label","CheckBox", "ComboBox", "ProgressBar"}
            ctrl_i = 0
            for ui in UIs:
                self.cl_d.append(ctrllist.AppendItem(self.cl_d[win_i], ui))
                self.cl_names.append({ui+".root", "root"})
                ctrl_i = i
                i += 1
                for ctrl_name in ui_d[ui]:
                    self.cl_d.append(ctrllist.AppendItem(
                        self.cl_d[ctrl_i], ctrl_name))
                    self.cl_names.append({win_name, ui, ctrl_name})
                    i += 1

    def CtrlList_Clicked(self, event):
        ClickedItem_Name = self.CtrlList.GetItemText(event.GetItem())
        print(ClickedItem_Name)
        if(ClickedItem_Name != "Windows"):
            # 選択した物は'Window'ではない
            ClickedItemParent = self.CtrlList.GetItemParent(event.GetItem())
            ClickedItemParent_Name = self.CtrlList.GetItemText(
                ClickedItemParent)
            if ClickedItemParent_Name != "Windows":
                # 選択した物はウインドウの名前でもない
                ClickedItemParentParent = self.CtrlList.GetItemParent(
                    ClickedItemParent)
                ClickedItemParentParent_Name = self.CtrlList.GetItemText(
                    ClickedItemParentParent)
                if ClickedItemParentParent_Name != "Windows":
                    # 選択した物はコントロールの種類でもない　つまり　コントロールの名前
                    f = open(ClickedItemParentParent_Name + '.json')
                    ui_d = json.load(f)
                    ClickedItem_d = ui_d[ClickedItemParent_Name][ClickedItem_Name]
                    print(ClickedItem_d)
                    d_len = len(ClickedItem_d)

                    # resize
                    row_len = self.CtrlInfoGrid.GetNumberRows()
                    if row_len != d_len:
                            if row_len < d_len:
                                need_len = d_len - row_len
                                self.CtrlInfoGrid.AppendRows(need_len)
                            else:
                                need_len = row_len - d_len
                                self.CtrlInfoGrid.DeleteRows(need_len)
                    #self.CtrlInfoGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGED,self.CtrlInfoGrid_Clicked())
                    self.CtrlInfoGrid.SetColSize(0, 50)
                    count = 0
                    for PropKind in ClickedItem_d:
                        self.CtrlInfoGrid.SetRowLabelValue(count, PropKind)
                        self.CtrlInfoGrid.SetCellValue(
                            count, 0, str(ClickedItem_d[PropKind]))
                        # self.CtrlInfoGrid.SetReadOnly(count,0,True)
                        count += 1
            else:
                # 選択した物はウインドウの名前
                # ウインドウの情報を表示
                a = 1

        
    def CtrlInfoGrid_Clicked(self,event):
        print("Clicked")


app = wx.App(False)
frame = MainWindow(None, "MouseEvents")
frame.Show()

app.MainLoop()
