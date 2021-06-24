# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:34:16 2021

@author: misum
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QMainWindow, QPushButton, QVBoxLayout, QFileDialog
import os
import re 

class Functions:
    def __init__(self):
        self.fileName = None
        self.fileContent = ""
        

    def getAnnotationFolder(self, MainWindow):
        options = QtWidgets.QFileDialog.Options()
        filename = QFileDialog.getExistingDirectory(None, 
        "Select ", options=options)

        if filename:
            print(filename)
            clean_filename = (str(filename))
            print("cleaned filename:", clean_filename)
            return clean_filename
        else:
            print("no")
        
        ##DEPRECIATED
    def getFastaFile(self, flank):
        options = QtWidgets.QFileDialog.Options()
        filename = QFileDialog.getOpenFileName(None, 
        "QFileDialog.getOpenFileName()", "Open file","FASTA Files (*.fasta *.fsa);;Text Files (*.txt)", options=options)

        if filename:
            print(filename)
            clean_filename = (str(filename[0]))
            print("cleaned filename::", clean_filename)
            return clean_filename
        else:
            print("no")
    
    
    def flankIdentifier(self, flank, MainWindow):
        cleaned_flank = flank.lower()
        f_format = None
        #checking flank input properties
        if (' ') in cleaned_flank:
            whiteSpaceDetect = True
        else:
            whiteSpaceDetect = False
        digitCheck = re.search(r'\d+$', cleaned_flank)
        
        if whiteSpaceDetect == True:
            f_format = str('product')
        elif whiteSpaceDetect == False and cleaned_flank.startswith('wp'):
            f_format = str('protein_id')
        elif whiteSpaceDetect == False and digitCheck is not None:
            f_format = str('locus_tag')
        else:
            print('cant be identified')
        return f_format
    
    def determineRange(self, location1, location2, MainWindow):
        miu = (min(f1_loc))
        mau = (max(f1_loc))
        mia = (min(f2_loc))
        maa = (max(f2_loc))
                    
        locusvals = [miu,mau,mia,maa]
        loc_max = (max(locusvals))
        loc_min = (min(locusvals))
                
        print("Locus minimum:",loc_min)
        print("Locus maximum:",loc_max)