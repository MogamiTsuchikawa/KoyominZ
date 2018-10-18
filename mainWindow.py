#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

btns = []
defalt_btn_info = {"locationX":0 , "locationY":0}
btns_info = []
class Button01(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        i = 0
        while i<2:
            btns.append(QPushButton("Btn"+str(i), self))
            btns[i].setText("Btn"+str(i))
            btns_info.append(defalt_btn_info)
            btns[i].move(90*i,40)
            btns_info[i]["locationX"]=90*i
            btns_info[i]["locationY"]=40
            i+=1

        btns[0].clicked.connect(self.button01Clicked)
        self.statusBar()
        
        self.setWindowTitle('Button01')
        self.show()

    def button01Clicked(self):
        sender = self.sender()
        btns[0].move(0,btns_info[0]["locationY"]+10)
        btns_info[0]["locationY"]+=10
        self.statusBar().showMessage(sender.text() + ' Push Button01'+str(btns[0].locale))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Button01()
    
    sys.exit(app.exec_())