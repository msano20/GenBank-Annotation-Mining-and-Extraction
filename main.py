# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:15:13 2021
@author: misum
"""
import sys
from PyQt5 import QtWidgets, uic
from mainwindow import Ui_MainWindow

class MainWindowUIClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__ (self):
        super(MainWindowUIClass, self).__init__(parent = None)
        uic.loadUi('mainwindow.ui', self)
        self.show()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUi(Ui_MainWindow())
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
