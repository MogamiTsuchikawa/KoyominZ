import json,wx
ui_d_s = {}

def Set_ui_d(gui_list,proj_direc):
    for f_name in gui_list:
        f = open(proj_direc + f_name,'r')
        ui_d_s[f_name.replace(".json","")] = json.load(f)
		