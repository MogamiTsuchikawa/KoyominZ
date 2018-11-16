import wx,json,numba,xmltodict
import xml.etree.ElementTree as ET

class Convert():
    def __init__(self,target_file):
        print("Converting "+target_file)
        self.target_file = target_file
        f = open(self.target_file,'r')
        self.ui_d = json.load(f)
        f.close()
        self.Convert_CS(target_file)
    def Convert_CS(self,target_file):
        target_file = target_file.rstip(".json")
        target_file = target_file + "_F.cs"
        sf = open(target_file,'w')
        
        

def get_CS_using(project_path,target_file,project_name):
    f = open(project_path+"/"+project_name+".csproj",'r')
    proj_d = ET.fromstring(f.read())
    f.close()




