# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:15:13 2021
might have to resort to placing all the functions in the mainwindow file
@author: misum
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QMainWindow, QPushButton, QVBoxLayout, QFileDialog
#from functions import Functions

##QtWidgets.QMainWindow,Ui_MainWindow
## QtWidgets.QWidget, Ui_MainWindow
class MainWindowUIClass(QtWidgets.QWidget, Ui_MainWindow):
    def __init__ (self):
        super(MainWindowUIClass, self).__init__(parent = None)
        #self.setupUi(self)
        #ui = MainWindowUIClass()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUi(Ui_MainWindow())
        #self.mainwindow = Ui_MainWindow()
        
        
        
    def returnPressedSlot1(self):
        flank1file = self.QLineEdit.getText()
        try:
            flank1file = open(flank1file, 'r').read()
            #self.setFileName(self.lineEdit.text())
            self.fileInput1 = flank1file
            print(flank1file)
            #flank_1 = self.lineEdit.text()
        except:
            print("fds")
    
    def returnPressedSlot2(self):
        flank_2 = self.PyQt5.QLineEdit.text()
        
    def getfile(self):
        options = QtWidgets.QFileDialog.Options()
        filename = QFileDialog.getOpenFileName(None, 
        "QFileDialog.getOpenFileName()", "Open file","FASTA Files (*.fasta *.fsa);;Text Files (*.txt)", options=options)

        if filename:
            print(filename)
        
    def browseSlot2(self):
        pass
    
    def InputFolderSlot(self):
        pass
    
    def ReturnPressed_Input(self):
        pass
    
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
