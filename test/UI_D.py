import json,wx
ui_d_s = {}

def Set_ui_d(gui_list,proj_direc):
	for f_name in gui_list:
		#f = open(proj_direc +"/"+ f_name + ".json",'r')
		f = open(f_name + ".json",'r')
		ui_d_s[f_name] = json.load(f)
