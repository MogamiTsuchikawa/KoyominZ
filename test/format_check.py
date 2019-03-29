import json,const

def format_check(Target_UI_Kind,ChangeKind,ChangeValue):
    if ChangeKind == "position" or ChangeKind == "size":
        check_o = str(ChangeValue)
        check_o1 = check_o.split(',')
        if len(check_o1) != 2:
            return "Erorr:区切り文字(,)の数が1でないです"
        elif not(check_o1[0].isdecimal()) or not(check_o1[1].isdecimal()):
            return "Erorr:指定にアラビア数字以外が使用されています"
        return "OK"
    if ChangeKind == "background_color" or  ChangeKind == "foreground_color":
        check_o = ChangeValue.split(',')
        if check_o[0] == "sys_color":
            if len(check_o) == 2:
                if check_o[1] in const.System_Color:
                    return "OK"
                else:
                    return "Erorr:システム定義色で定義されていません"
            else:
                return "Erorr:データ転送フォーマットが間違っています。"
        else:
            #RGBでの指定
            if len(check_o) == 4:
                return "OK"
            else:
                return "Erorr:データ転送フォーマットが間違っています。"




