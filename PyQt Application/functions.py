# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:34:16 2021

@author: misum
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QMainWindow, QPushButton, QVBoxLayout, QFileDialog
    
class Functions:
    def __init__(self):
        self.fileName = None
        self.fileContent = ""
        

    def getfile(self, MainWindow):
        options = QtWidgets.QFileDialog.Options()
        filename = QFileDialog.getOpenFileName(None, 
        "QFileDialog.getOpenFileName()", "Open file","FASTA Files (*.fasta *.fsa);;Text Files (*.txt)", options=options)

        if filename:
            print(filename)
            #print(self.fileInput1)
            #print(self.fileInput1)
            #return self.flank1Upload.text()
            #flank1Upload.text()
            clean_filename = (str(filename[0]))
            print("cleaned filename::", clean_filename)
            return clean_filename
        else:
            print("no")

   