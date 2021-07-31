# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

'''
need to account for instances where there is a \n

account for genes coming from different strands

update textEdit and progressbar
'''
import os
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QMainWindow, QPushButton, QVBoxLayout, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QBasicTimer
import sys, time
from functions import Functions
import logging
import csv
from Bio import SeqIO

logging.basicConfig(filename='Errors.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

csv_headers = ['Species', 'Group', 'Strain', 'Chr', 'Accession', 'LocusTag', 'ProtID', 'Seq']


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.productLabel = QtWidgets.QLabel(self.centralwidget)
        self.productLabel.setGeometry(QtCore.QRect(370, 230, 61, 21))
        self.productLabel.setObjectName("productLabel")
        self.qualifiers = QtWidgets.QLabel(self.centralwidget)
        self.qualifiers.setGeometry(QtCore.QRect(50, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.qualifiers.setFont(font)
        self.qualifiers.setObjectName("qualifiers")
        self.oldLocus_label = QtWidgets.QLabel(self.centralwidget)
        self.oldLocus_label.setGeometry(QtCore.QRect(50, 230, 71, 21))
        self.oldLocus_label.setObjectName("oldLocus_label")
        self.protid_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.protid_Input.setGeometry(QtCore.QRect(450, 200, 221, 21))
        self.protid_Input.setText("")
        self.protid_Input.setObjectName("protid_Input")
        self.flankInput2 = QtWidgets.QLineEdit(self.centralwidget)
        self.flankInput2.setGeometry(QtCore.QRect(180, 130, 491, 21))
        self.flankInput2.setObjectName("flankInput2")
        self.flankInput1 = QtWidgets.QLineEdit(self.centralwidget)
        self.flankInput1.setGeometry(QtCore.QRect(180, 100, 491, 21))
        self.flankInput1.setObjectName("flankInput1")
        self.protid_label = QtWidgets.QLabel(self.centralwidget)
        self.protid_label.setGeometry(QtCore.QRect(370, 200, 61, 21))
        self.protid_label.setObjectName("protid_label")
        self.locus_label = QtWidgets.QLabel(self.centralwidget)
        self.locus_label.setGeometry(QtCore.QRect(50, 200, 51, 21))
        self.locus_label.setObjectName("locus_label")
        #self.gene_nameInput = QtWidgets.QLineEdit(self.centralwidget)
        #self.gene_nameInput.setGeometry(QtCore.QRect(450, 230, 221, 21))
        #self.gene_nameInput.setText("")
        #self.gene_nameInput.setObjectName("gene_nameInput")
        self.extractbtn = QtWidgets.QPushButton(self.centralwidget)
        self.extractbtn.setGeometry(QtCore.QRect(270, 280, 191, 41)) #270, 300, 191, 41
        self.extractbtn.setObjectName("extractbtn")
        self.oldlocus_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.oldlocus_Input.setGeometry(QtCore.QRect(130, 230, 221, 21))
        self.oldlocus_Input.setText("")
        self.oldlocus_Input.setObjectName("oldlocus_Input")
        self.geneName_label = QtWidgets.QLabel(self.centralwidget)
        #self.geneName_label.setGeometry(QtCore.QRect(370, 230, 61, 21))
        #self.geneName_label.setObjectName("geneName_label")
        self.product_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.product_Input.setGeometry(QtCore.QRect(450, 230, 221, 21))
        self.product_Input.setText("")
        self.product_Input.setObjectName("product_Input")
        self.locuslabel_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.locuslabel_Input.setGeometry(QtCore.QRect(130, 200, 221, 21))
        self.locuslabel_Input.setText("")
        self.locuslabel_Input.setObjectName("locuslabel_Input")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 350, 621, 150)) #50, 359, 621, 81
        self.textEdit.setObjectName("textEdit")
        #self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        #self.progressBar.setGeometry(QtCore.QRect(50, 460, 621, 16))
        #self.progressBar.setProperty("value", 0)
        #self.progressBar.setObjectName("progressBar")
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
        self.locus_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.locus_label_2.setGeometry(QtCore.QRect(50, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.locus_label_2.setFont(font)
        self.locus_label_2.setObjectName("locus_label_2")
        self.locus_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.locus_label_3.setGeometry(QtCore.QRect(50, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.locus_label_3.setFont(font)
        self.locus_label_3.setObjectName("locus_label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.FolderUpload.clicked.connect(lambda: self.InputFolderSlot(self, MainWindow))
        self.extractbtn.clicked.connect(lambda: self.extract(self))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.productLabel.setText(_translate("MainWindow", "Product"))
        self.qualifiers.setText(_translate("MainWindow", "Qualifiers"))
        self.oldLocus_label.setText(_translate("MainWindow", "Old Locus Tag"))
        self.protid_label.setText(_translate("MainWindow", "Protein ID"))
        self.locus_label.setText(_translate("MainWindow", "Locus Tag"))
        self.extractbtn.setText(_translate("MainWindow", "Extract"))
        #self.geneName_label.setText(_translate("MainWindow", "Gene Name"))
        self.FolderUpload.setText(_translate("MainWindow", "Input Folder"))
        self.title.setText(_translate("MainWindow", "Gene Extraction"))
        self.locus_label_2.setText(_translate("MainWindow", "Flank 1 Identifier"))
        self.locus_label_3.setText(_translate("MainWindow", "Flank 2 Identifier"))


    def browseSlot1( self, filename, MainWindow ):
        inputFile1 = Functions.getFastaFile(filename, MainWindow)
        self.flankInput1.setText(str(inputFile1))
        #print("input1File name:  ", inputFile1)

        
    #@pyqtSlot()
    def browseSlot2(self, clean_filename, MainWindow):
        inputFile2 = Functions.getFastaFile(clean_filename, MainWindow)
        self.flankInput2.setText(str(inputFile2))
    
    #@pyqtSlot()
    def InputFolderSlot(self, clean_filename, MainWindow):
        inputFile = Functions.getAnnotationFolder(self, MainWindow)
        self.FolderInput.setText(str(inputFile))
        #print("file name: %s", inputFile)
    
    #@pyqtSlot()
    def extract(self, MainWindow):
        '''
        locusLabel= self.locuslabel_Input.text()
        oldLocus = self.oldlocus_Input.text()
        product = self.product_Input.text()
        protID = self.protid_Input.text()
        #geneName = self.gene_nameInput.text()
        '''
        
        flank_1 = self.flankInput1.text()
        flank_2 = self.flankInput2.text()
        targetCustomization = dict(locus_tag=self.locuslabel_Input.text(), old_locus_tag=self.oldlocus_Input.text(),
                                   product=self.product_Input.text(), protein_id = self.protid_Input.text()) 
                                   #gene = self.gene_nameInput.text())
        print("target customization variable:", targetCustomization)
        #print(targetCustomization)
        searchTerms = Functions.searchInterpreter(self, targetCustomization, MainWindow)
        print(searchTerms)
        
        #The output is written in the same folder as the input
        outputLocation = self.FolderInput.text()
        
        
        print("flank1:", flank_1)
        print("flank2:", flank_2)
        
        print("flank1 type:", type(flank_1))
        
        flankFormat1 = Functions.flankIdentifier(self, flank_1, MainWindow)
        flankFormat2 = Functions.flankIdentifier(self, flank_2, MainWindow)
        
        print("flank1 format:", flankFormat1)
        print("flank2 format:", flankFormat2)
        
        #raise flag if no search terms were entered by user
        emptyDict = all(x==None for x in searchTerms.items())
        print("emptydict status:", emptyDict)
        
        self.textEdit.append("Scanning %s..." % outputLocation)
        fileProgress = 0
        totalFileCount = 0
        fileFailureCount = 0
        for root, dirs, assembly in os.walk(outputLocation, topdown=True):
            for strain in assembly:
                strain = os.path.join(root, strain)
                if strain.endswith('.gbff'):
                    flank1matches = 0
                    flank2matches = 0
                    totalFileCount += 1
                    #annotFile = SeqIO.parse(strain, 'gb')
                    for record in SeqIO.parse(strain, "gb"): #prints seqs for all three chromosomes
                        
                        #print(record.seq[:20])
                        for feature in record.features:
                        #print(feature.source)
                            if feature.type == "CDS":
                                try:
                                    if feature.qualifiers['%s' % flankFormat1][0] == flank_1:
                                        f1_loc = feature.location
                                        f1_desc = record.description
                                        flank1matches += 1
                                        print("found 1 %s", f1_loc)
                                    if feature.qualifiers['%s' % flankFormat2][0] == flank_2:
                                        f2_loc = feature.location
                                        f2_desc = record.description
                                        flank2matches += 1
                                        print("found 2 %s", f2_loc)
                                except:
                                    pass
                                '''
                                if feature.qualifiers['%s' % flankFormat1][0] == flank_1:
                                if feature.qualifiers['%s' % flankFormat2][0] == flank_2:
                                '''
               
                    #if flank1matches or flank2matches > 2:
                    if flank1matches > 1 or flank2matches > 1:
                        
                        print("Multiple flanks match description. Consider using more unique identifiers")
                        print("flank1's found:", flank1matches)
                        print("flank2's found:", flank2matches)
                        continue
                    
                    else:
                        try:
                            loc_min, loc_max = Functions.determineRange(self, f1_loc, f2_loc, MainWindow)
                            print("flanks found in %s" % strain)
                            print("Locus minimum:",loc_min)
                            print("Locus maximum:",loc_max)
                        except:
                            print("flank not determined")
                            #logging.error('%s Flank locations could not be determined' % (strain))
                            continue
                        
                    #!!!self.textEdit.append("%s GenBank annotation files found.")
                    #!!!self.progressBar.setRange(0, totalFileCount)
                    print("total file count:", totalFileCount)
                    
                    #search process
                    candidate = [] #contains the gene of interest
                    
                    for root, dirs, assembly in os.walk('.', topdown=True):
                        for strain in assembly:
                            strain = os.path.join(root, strain)
                            if strain.endswith('.gbff'):
                                fileProgress += 1
                                time.sleep(0.05)
                                #self.progressBar.setValue(fileProgress)
                                QtCore.QCoreApplication.processEvents()
                                for record in SeqIO.parse(strain, "gb"):
                                    if record.description == f1_desc == f2_desc:
                                        gene_desc = record.description
                                        print(gene_desc)
                                        for feature in record.features:
                                            if feature.type == "CDS":
                                                if min(feature.location) in range(loc_min,loc_max):
                                                    #print("SEARCH TERMS keys:",searchTerms.keys())
                                                    
                                                    if emptyDict == False:
                                                        for key, value in searchTerms.items():
                                                            #print("key:", key)
                                                            #print("value:", value)
                                                            #print("---")
                                                            if feature.qualifiers['%s' % key][0] == value:
                                                                print('key found:' )
                                                                #print(key, value)
                                                                candidate.append(feature)
                                                        
                                                                record_info = record
                                                                source_feature = record.features[0]
                                                                source_qualifiers = source_feature.qualifiers
                                                                
                                                                try:
                                                                    rec_desc = record.description
                                                                except:
                                                                    rec_desc = ""
                                                                try:
                                                                    rec_id = record.id
                                                                except:
                                                                    rec_id = ""
                                                                
                                                            
                                                        #print(candidate)
                                                    elif emptyDict == True:
                                                        record_info = record
                                                        source_feature = record.features[0]
                                                        source_qualifiers = source_feature.qualifiers
                                                        candidate.append(feature)
                                                        try:
                                                            rec_desc = record.description
                                                        except:
                                                            rec_desc = ""
                                                        try:
                                                            rec_id = record.id
                                                        except:
                                                            rec_id = ""
                                        
                    print("PRINTING LIST OF CANDIDATES:", candidate)
                    print("-----------------------------------------")
                    
                    output_filename = (str(rec_id) + ' ' + str(rec_desc) + '.csv')
                    if candidate != []:
                        self.textEdit.append("Extracting %s genes from %s..." % (len(candidate), rec_desc))
                        #if len(candidate) <= max_homologs:
                        for item in candidate:
                            
                        #extract the following elements of the annotation file:
                            try:
                                c_species = record_info.annotations["taxonomy"][5] #species
                            except: 
                                c_species = float("NaN")
                                        
                            try: 
                                c_family = record_info.annotations["taxonomy"][6] #strain (if available)
                            except: 
                                c_family = float("NaN")
                                        
                            try:
                                c_strain = str(source_qualifiers["strain"])
                                c_strain_raw = c_strain.strip("[\']")
                                #c_strain = record.annotations['organism']
                            except: 
                                c_strain_raw = float("NaN")
                                        
                            try: 
                                c_chr = str(source_qualifiers["chromosome"]) #(as an integer)
                                c_chr_raw = c_chr.strip("[\']")
                            except: 
                                c_chr_raw = float("NaN")
                                      
                                            
                            try:
                                c_locustag = str(item.qualifiers["locus_tag"])
                                c_locustag_raw = c_locustag.strip("[\']")
                            except:
                                c_locustag_raw = float("NaN")
                                            
                            try:
                                protid = str(item.qualifiers['protein_id'])
                                raw_protid = protid.strip("[\']") 
                            except: 
                                raw_protid =  float("NaN")
                            '''
                            try:
                                gene_name = str(item.qualifiers['gene'])
                                raw_gene_name = gene_name.strip("[\']")
                            except:
                                raw_gene_name = float("NaN")
                            try:
                                #rec_desc = record.description
                                print("record desc:", rec_desc)
                            except:
                                rec_desc = float("NaN")
                                
                            try:
                                #rec_id = record.id
                                print("record ID:", rec_id)
                            except:
                                rec_id = float("NaN")
                            '''
                            try:
                                gene_seq = (item.qualifiers['translation'][0])
                            except:
                                gene_seq = float("NaN")
                                #logging.error('%s %s sequence information unavailable' % (gene_desc, strain))
                                
                            print("printing new row: ==============================")
                            print(c_species, c_family, c_strain_raw, c_chr_raw, rec_id, c_locustag_raw, raw_protid, gene_seq)                  
                            new_row = [c_species, c_family, c_strain_raw, c_chr_raw, rec_id, c_locustag_raw, raw_protid, gene_seq]
                            
                            
                            
                            print(output_filename)
                            with open(output_filename, 'a', newline='') as csvfile:  
                                writer = csv.writer(csvfile)
                                writer.writerow(new_row)
                                csvfile.close()
                                
                            
                else:
                    print("No genes within locus fit the product description")
                    #logging.error('%s %s No genes within locus fit the product description' % (gene_desc, strain))
                
                                              
        self.textEdit.append("Extraction finished.")
        #return loc_min, loc_max, f1_desc, f2_desc
        
        #loc_min, loc_max, f1_desc, f2_desc = flanksearch()

'''
    def __init__(self):
        self.fileName = None
        self.fileContent = ""

'''   
