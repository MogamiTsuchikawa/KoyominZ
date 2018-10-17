#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Button01(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        

        btns = []
        i = 0

        while i<2:
            btns.append(QPushButton("Btn"+str(i), self))
            btns[i].setText("Btn"+str(i))
            btns[i].move(20 + 90*i,40)
            i+=1
        
        self.statusBar()

        self.setWindowTitle('Button01')
        self.show()

    def button01Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Push Button01')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Button01()
    sys.exit(app.exec_())