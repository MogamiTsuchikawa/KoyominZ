import wx,json,numba

class Convert():
    def __init__(self,target_file):
        print("Converting "+target_file)
        self.target_file = target_file
        f = open(self.target_file,'r')
        self.ui_d = json.load(f)
        self.Convert_CS()
    def Convert_CS():
        