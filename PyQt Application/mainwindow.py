# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

#from . import functions
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QMainWindow, QPushButton, QVBoxLayout, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import sys
from functions import Functions

class Ui_MainWindow(QObject): #used to be object
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.flank2Upload = QtWidgets.QPushButton(self.centralwidget)
        self.flank2Upload.setGeometry(QtCore.QRect(50, 130, 101, 21))
        self.flank2Upload.setObjectName("flank2Upload")
        self.productLabel = QtWidgets.QLabel(self.centralwidget)
        self.productLabel.setGeometry(QtCore.QRect(50, 260, 41, 21))
        self.productLabel.setObjectName("productLabel")
        self.qualifiers = QtWidgets.QLabel(self.centralwidget)
        self.qualifiers.setGeometry(QtCore.QRect(50, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.qualifiers.setFont(font)
        self.qualifiers.setObjectName("qualifiers")
        self.oldLocus_label = QtWidgets.QLabel(self.centralwidget)
        self.oldLocus_label.setGeometry(QtCore.QRect(50, 230, 71, 21))
        self.oldLocus_label.setObjectName("oldLocus_label")
        self.protid_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.protid_Input.setGeometry(QtCore.QRect(450, 200, 221, 21))
        self.protid_Input.setText("")
        self.protid_Input.setObjectName("protid_Input")
        self.fileInput2 = QtWidgets.QLineEdit(self.centralwidget)
        self.fileInput2.setGeometry(QtCore.QRect(180, 130, 491, 21))
        self.fileInput2.setObjectName("fileInput2")
        self.flank1Upload = QtWidgets.QPushButton(self.centralwidget)
        self.flank1Upload.setGeometry(QtCore.QRect(50, 100, 101, 21))
        self.flank1Upload.setObjectName("flank1Upload")
        self.fileInput1 = QtWidgets.QLineEdit(self.centralwidget)
        self.fileInput1.setGeometry(QtCore.QRect(180, 100, 491, 21))
        self.fileInput1.setObjectName("fileInput1")
        self.protid_label = QtWidgets.QLabel(self.centralwidget)
        self.protid_label.setGeometry(QtCore.QRect(370, 200, 61, 21))
        self.protid_label.setObjectName("protid_label")
        self.locus_label = QtWidgets.QLabel(self.centralwidget)
        self.locus_label.setGeometry(QtCore.QRect(50, 200, 51, 21))
        self.locus_label.setObjectName("locus_label")
        self.gene_nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.gene_nameInput.setGeometry(QtCore.QRect(450, 230, 221, 21))
        self.gene_nameInput.setText("")
        self.gene_nameInput.setObjectName("gene_nameInput")
        self.extractbtn = QtWidgets.QPushButton(self.centralwidget)
        self.extractbtn.setGeometry(QtCore.QRect(270, 300, 191, 41))
        self.extractbtn.setObjectName("extractbtn")
        self.oldlocus_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.oldlocus_Input.setGeometry(QtCore.QRect(130, 230, 221, 21))
        self.oldlocus_Input.setText("")
        self.oldlocus_Input.setObjectName("oldlocus_Input")
        self.geneName_label = QtWidgets.QLabel(self.centralwidget)
        self.geneName_label.setGeometry(QtCore.QRect(370, 230, 61, 21))
        self.geneName_label.setObjectName("geneName_label")
        self.product_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.product_Input.setGeometry(QtCore.QRect(130, 260, 221, 21))
        self.product_Input.setText("")
        self.product_Input.setObjectName("product_Input")
        self.locuslabel_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.locuslabel_Input.setGeometry(QtCore.QRect(130, 200, 221, 21))
        self.locuslabel_Input.setText("")
        self.locuslabel_Input.setObjectName("locuslabel_Input")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 359, 621, 81))
        self.textEdit.setObjectName("textEdit")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 460, 621, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.FolderUpload = QtWidgets.QPushButton(self.centralwidget)
        self.FolderUpload.setGeometry(QtCore.QRect(50, 60, 101, 21))
        self.FolderUpload.setObjectName("FolderUpload")
        self.FolderInput = QtWidgets.QLineEdit(self.centralwidget)
        self.FolderInput.setGeometry(QtCore.QRect(180, 60, 491, 21))
        self.FolderInput.setObjectName("FolderInput")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(270, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.title.setFont(font)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #MainWindow.browseSlot2
        self.retranslateUi(MainWindow)
        self.flank1Upload.clicked.connect(lambda: self.browseSlot1(self, MainWindow))
        self.flank2Upload.clicked.connect(lambda: self.browseSlot2(self, MainWindow))
        self.FolderUpload.clicked.connect(lambda: self.InputFolderSlot(self, MainWindow))
        self.extractbtn.clicked.connect(lambda: self.extract(self))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flank2Upload.setText(_translate("MainWindow", "Upload Flank 2"))
        self.productLabel.setText(_translate("MainWindow", "Product"))
        self.qualifiers.setText(_translate("MainWindow", "Qualifiers"))
        self.oldLocus_label.setText(_translate("MainWindow", "Old Locus Tag"))
        self.flank1Upload.setText(_translate("MainWindow", "Upload Flank 1"))
        self.protid_label.setText(_translate("MainWindow", "Protein ID"))
        self.locus_label.setText(_translate("MainWindow", "Locus Tag"))
        self.extractbtn.setText(_translate("MainWindow", "Extract"))
        self.geneName_label.setText(_translate("MainWindow", "Gene Name"))
        self.FolderUpload.setText(_translate("MainWindow", "Input Folder"))
        self.title.setText(_translate("MainWindow", "Gene Extraction"))
        
    def browseSlot1( self, filename, MainWindow ):
        inputFile1 = Functions.getfile(filename, MainWindow)
        self.fileInput1.setText(str(inputFile1))
        #print("input1File name:  ", inputFile1)

        
    #@pyqtSlot()
    def browseSlot2(self, clean_filename, MainWindow):
        inputFile2 = Functions.getfile(clean_filename, MainWindow)
        self.fileInput2.setText(str(filename[0]))
    
    #@pyqtSlot()
    def InputFolderSlot(self, clean_filename, MainWindow):
        inputFile = Functions.getfile(clean_filename, MainWindow)
        self.FolderInput.setText(str(inputFile2))
        #print("file name: %s", inputFile)
    
    #@pyqtSlot()
    def extract(self, MainWindow):
        locusLabel= self.locuslabel_Input.text()
        oldLocus = self.oldlocus_Input.text()
        product = self.product_Input.text()
        protID = self.protid_Input.text()
        geneName = self.gene_nameInput.text()
        
        outputLocation = self.Folder.Input.text()
        flank_1 = self.fileInput1.text()
        flank_2 = self.fileInput2.text()
        
        print(inputFile1)
        #print(str("inputfile: %s", inputFile1))
        print(locusLabel)

'''
    def __init__(self):
        self.fileName = None
        self.fileContent = ""
'''   

    