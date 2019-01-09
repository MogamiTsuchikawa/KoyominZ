import json,wx,const
ui_d_s = {}
rtn_ui_d = {}

def Set_ui_d(gui_list,proj_direc):
	for f_name in gui_list:
		#f = open(proj_direc +"/"+ f_name + ".json",'r')
		f = open(const.project_dir+"\\"+ f_name + ".gson",'r')
		ui_d_s[f_name] = json.load(f)
def Make_ui_d(name):
	rtn_ui_d = {}
	rtn_ui_d["Window"] = {"name":name,"size":{"X":600,"Y":500},"text":name}
	rtn_ui_d["Button"] = {"btn":{"position":{"X":300,"Y":300},"text":"ボタン"}}
	return rtn_ui_d