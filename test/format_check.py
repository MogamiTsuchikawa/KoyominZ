import json

def format_check(Target_UI_Kind,ChangeKind,ChangeValue):
    if(ChangeKind == "position" or ChangeKind == "size"):
        check_o = str(ChangeValue)
        check_o1 = check_o.split(',')
        if len(check_o1) != 2:
            return "Erorr:区切り文字(,)の数が1でないです"
        elif not(check_o1[0].isdecimal()) or not(check_o1[1].isdecimal()):
            return "Erorr:指定にアラビア数字以外が使用されています"
        return "OK"
