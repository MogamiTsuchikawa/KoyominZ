import wx,json,copy,asyncio,threading,wx.grid,numba
import DesignWindow,const,convert,UI_D

class MainWindow(wx.Frame):
    #@numba.jit
    def __init__(self, parent, title,testmode):
        #[0]にウインドウの名前,[1]に現在表示しているプロパティのコントロールの種類(ex:Button),[2]にコントロールの名前を保管
        self.list_selected_ctrl = ["","KIND","NAME"]
        self.selected_ui_d = {}
        self.Preview_Windows = {}
        self.Preview_Window_IDs = {}
        if testmode:
            self.window_list = ["gui"] #動作試験用に確保。今後削除
            self.proj_direc = "TEST"
        else:
            self.window_list = const.source_files['gson']
            self.proj_direc = const.project_dir
        
        
        UI_D.Set_ui_d(self.window_list,self.proj_direc)
        wx.Frame.__init__(self, parent, title=title)
        self.SetSize(500, 600)
        panel = wx.Panel(self, wx.ID_ANY)
        #MenuBar追加処理
        menu_bar = wx.MenuBar()
        menu_items = []
        menu_items_i = 0
        #FILE MENU
        menu_file = wx.Menu()
        for m_text in ["New","Open","Save","Save As"]:
            menu_items.append(wx.MenuItem(menu_file,menu_items_i+1,m_text))
            menu_file.AppendItem(menu_items[menu_items_i])
            menu_items_i +=1
        #EDIT MENU
        menu_edit = wx.Menu()
        for m_text in ["Cut","Copy","Paste"]:
            menu_items.append(wx.MenuItem(menu_edit,menu_items_i+1,m_text))
            menu_edit.AppendItem(menu_items[menu_items_i])
            menu_items_i +=1
        #MAKE MENU
        menu_make = wx.Menu()
        for m_text in ["MakeCS","Build"]:
            menu_items.append(wx.MenuItem(menu_make,menu_items_i+1,m_text))
            menu_make.AppendItem(menu_items[menu_items_i])
            menu_items_i +=1
        #CTRL MENU
        menu_ctrl = wx.Menu()
        for m_text in ["Add Ctrl"]:
            menu_items.append(wx.MenuItem(menu_ctrl,menu_items_i+1,m_text))
            menu_ctrl.AppendItem(menu_items[menu_items_i])
            menu_items_i += 1
        menu_bar.Append(menu_file,"File")
        menu_bar.Append(menu_edit,"Edit")
        menu_bar.Append(menu_make,"Make")
        menu_bar.Append(menu_ctrl,"Ctrl")
        self.SetMenuBar(menu_bar)
        #menu_bar_items[menu_bar_items_i].Bind(wx.EVT_MENU,self.Menu_Make_Clicked)
        self.Bind(wx.EVT_MENU,self.Menu_Clicked)
        #self.Show(True)
        #
        StaBar = self.CreateStatusBar()
        #デザインウインドウの表示 Show_Preview_Windowメソッドに移行
        #self.Preview_Window = DesignWindow.DesignWindow(self, "MousePoint")
        #self.Preview_Window_ID = self.Preview_Window.Show()


        self.CtrlList = wx.TreeCtrl(panel, -1, pos=(0, 20))
        self.CtrlList.Size = (200, 400)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,self.CtrlList_Clicked, self.CtrlList)
        self.SetCtrlList(self.CtrlList)

        self.tab_view = wx.Notebook(panel,wx.ID_ANY,pos=(210,20))
        self.tab_view.Size = (200,400)
        self.CtrlInfoGrid_Panel = wx.Panel(self.tab_view,wx.ID_ANY)
        self.EvtInfoGrid_Panel = wx.Panel(self.tab_view,wx.ID_ANY)
        self.tab_view.AddPage(self.CtrlInfoGrid_Panel,"プロパティ")
        self.tab_view.AddPage(self.EvtInfoGrid_Panel,"イベント")

        self.CtrlInfoGrid = wx.grid.Grid(self.CtrlInfoGrid_Panel,-1,pos=(0,0))
        self.CtrlInfoGrid.CreateGrid(1, 1)
        self.CtrlInfoGrid.Size = (200, 400)
        self.CtrlInfoGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGED,self.CtrlInfoGrid_Changed)

        self.EvtInfoGrid = wx.grid.Grid(self.EvtInfoGrid_Panel,-1,pos=(0,0))
        self.EvtInfoGrid.CreateGrid(1,1)
        self.EvtInfoGrid.Size=(200,400)
        for winname in self.window_list:
            self.Show_Preview_Window(winname)
            #pass
        
    def Show_Preview_Window(self,target_winname):
        self.Preview_Windows[target_winname] = DesignWindow.Design_Window(self,target_winname)
        self.Preview_Window_IDs[target_winname] = self.Preview_Windows[target_winname].Show()
        pass
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
            ui_d = UI_D.ui_d_s[win_name]
            ctrl_i = 0
            for ui in const.UIs:
                self.cl_d.append(ctrllist.AppendItem(self.cl_d[win_i], ui))
                self.cl_names.append({ui+".root", "root"})
                ctrl_i = i
                i += 1
                for ctrl_name in ui_d[ui]:
                    self.cl_d.append(ctrllist.AppendItem(
                        self.cl_d[ctrl_i], ctrl_name))
                    self.cl_names.append({win_name, ui, ctrl_name})
                    i += 1
    #@numba.jit
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
                    f = open(const.project_dir +"\\"+ ClickedItemParentParent_Name + '.gson')
                    self.selected_ui_d = json.load(f)
                    ClickedItem_d = self.selected_ui_d[ClickedItemParent_Name][ClickedItem_Name]
                    self.list_selected_ctrl[0] = ClickedItemParentParent_Name
                    self.list_selected_ctrl[1] = ClickedItemParent_Name
                    self.list_selected_ctrl[2] = ClickedItem_Name
                    print(ClickedItem_d)
                    d_len = len(ClickedItem_d)
                    # resize
                    row_len = self.CtrlInfoGrid.GetNumberRows()
                    if "event" in ClickedItem_d:
                        d_len -= 1
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
                        if PropKind != "event":
                            self.CtrlInfoGrid.SetRowLabelValue(count, PropKind)
                            self.CtrlInfoGrid.SetCellValue(
                                count, 0, str(ClickedItem_d[PropKind]))
                            count += 1
            else:
                # 選択した物はウインドウの名前
                # ウインドウの情報を表示
                a = 1
    def CtrlInfoGrid_Clicked(self,event):
        print("Clicked")
        tmp = event.GetId()
        print(tmp)
    def CtrlInfoGrid_Changed(self,event):
        print("hello")
        tmp = event.GetId()
        print(event.GetString())
        self.Search_Changed_Ctrl_Kind()
    def Search_Changed_Ctrl_Kind(self):
        props = self.selected_ui_d[self.list_selected_ctrl[1]][self.list_selected_ctrl[2]]
        for prop_kind in props:
            for i in range(len(props)):
                if prop_kind == self.CtrlInfoGrid.GetRowLabelValue(i):
                    if props[prop_kind] != self.CtrlInfoGrid.GetCellValue(i,0):
                        self.selected_ui_d[self.list_selected_ctrl[1]][self.list_selected_ctrl[2]][prop_kind] = self.CtrlInfoGrid.GetCellValue(i,0)
                        self.Preview_Window.ChangeCtrlValue(self.list_selected_ctrl[1], self.list_selected_ctrl[2], prop_kind, self.CtrlInfoGrid.GetCellValue(i,0))
    #MenuのMakeがクリックされたときに呼び出し
    def Menu_Clicked(self,event):
        Menu_No = event.GetId()
        print(Menu_No)
        if Menu_No == 1:
            self.File_New_Clicked()
        elif Menu_No == 2:
            self.File_Open_Clicked()
        elif Menu_No == 3:
            self.File_Save_Clicked()
        elif Menu_No == 4:
            self.File_SaveAs_Clicked()
        elif Menu_No == 5:
            self.Edit_Cut_Clicked()
        elif Menu_No == 6:
            self.Edit_Copy_Clicked()
        elif Menu_No == 7:
            self.Edit_Paste_Clicked()
        elif Menu_No == 8:
            self.Make_MakeCS_Clicked()
        elif Menu_No == 9:
            self.Make_Build_Clicked()
        elif Menu_No == 10:
            self.Ctrl_AddCtrl_Clicked()
    
    def File_New_Clicked(self):
        pass
    def File_Open_Clicked(self):
        pass
    def File_Save_Clicked(self):
        self.Preview_Window.Save()
    def File_SaveAs_Clicked(self):
        pass
    def Edit_Cut_Clicked(self):
        pass
    def Edit_Copy_Clicked(self):
        pass
    def Edit_Paste_Clicked(self):
        pass
    def Make_MakeCS_Clicked(self):
        conv = convert.Convert("gui.json","test")
    def Make_Build_Clicked(self):
        pass
    def Ctrl_AddCtrl_Clicked(self):
        pass
