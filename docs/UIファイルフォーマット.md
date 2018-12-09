
# JSONファイルフォーマット
サンプル

```JSON
{
    "Window":
    {
        "name":"sample window",
        "size":{"X":300,"Y":200},
        "text":"Hello"
    },
    "Button":
    {
        "Ctrl_Name":
        {
            "parent":"tab_ctrl_1",
            "position":{"X":0,"Y":0},
            "size":{"X":20,"Y":20},
            "text":"sample_text",
            "event":
            {
                "ON_CLICK":"btn_click_fun",
                "WINDOW_LOADED":"window_loaded_fun"
            }
        }
    }
}
```
## 基本
基本的に必ず指定が必要な設定項目はない。  
指定されない場合、デフォルトの値が指定される
ファイル名がそのままウインドウの名前になる

## デフォルトの値
以下にプロパティとデフォルトの値を表示する

プロパティ|デフォルト値|説明
:-:|:-:|:-:
parent|root|rootはウインドウの基本的なPanel、Pythonソースコード内ではroot_panelと記述する。
position|0,0|parentの(0,0)が指定される
size|20,20|指定間違えて見えなくなっても困るのでデフォルトは20,20。あまりに見えにくそうな値を指定するとエディタが呼びかける
text|{CTRL_NAME}|そのままコントロールの名前が指定される。


## コントロールの種類と可能なプロパティ  

以下にコントロール全種類の指定可能な設定項目を書くかも  
### Window
Window自体の設定項目を記入。無ければデフォルトの値を使用。  
また、ウインドウ名はファイル名が採用される。  
プロパティ|例|説明
:-:|:-:|:-:
name|Form1|ウインドウの名前
size|X:300,Y:200|ウインドウのサイズ(px)
text|Hello Window|ウインドウバー(Windows)へ表示するテキスト

### Button
