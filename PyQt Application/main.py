# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:15:13 2021
@author: misum
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject, pyqtSlot
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QMainWindow, QPushButton, QVBoxLayout, QFileDialog
#from functions import Functions

##QtWidgets.QMainWindow,Ui_MainWindow
## QtWidgets.QWidget, Ui_MainWindow
class MainWindowUIClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__ (self):
        super(MainWindowUIClass, self).__init__(parent = None)
        #self.setupUi(self)
        #ui = MainWindowUIClass()
        uic.loadUi('mainwindow.ui', self)
        self.show()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUi(Ui_MainWindow())
        #self.mainwindow = Ui_MainWindow()

    
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #ui = MainWindowUIClass()
    ui = Ui_MainWindow()
    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
