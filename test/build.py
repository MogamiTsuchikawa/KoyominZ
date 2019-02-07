import json,shutil,os
import const,convert

def Build_app():
    if const.project_kind == "dotnetcore_winform":
        Build_dotnetcore_winform()
def Build_dotnetcore_winform():
    for gson_f in const.source_files["gson"]:
        convert.Convert(gson_f+".gson",const.project_name)
        os.remove(const.project_dir + const.pathsep + const.project_name + const.pathsep + gson_f + ".Designer.cs")
        shutil.move(const.project_dir + const.pathsep + gson_f + ".Designer.cs",const.project_dir + const.pathsep + const.project_name + const.pathsep)
    os.system("cd " + const.project_dir + const.pathsep + const.project_name + " & dotnet build")
