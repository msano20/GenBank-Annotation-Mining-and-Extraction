# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:34:16 2021

@author: misum
"""
import re 
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from Bio import pairwise2

class Functions:
    def __init__(self):
        self.fileName = None
        self.fileContent = ""
        
    def getAnnotationFolder(self, MainWindow):
        options = QtWidgets.QFileDialog.Options()
        filename = QFileDialog.getExistingDirectory(None, 
        "Select ", options=options)

        if filename:
            clean_filename = (str(filename))
            return clean_filename
    
    def searchInterpreter(self, searchDictionary, MainWindow):
        #Determines which search fields contain terms. 
        newDictionary = {}
        for key, value in searchDictionary.items():
            if searchDictionary[key]:
                #print(value)
                newDictionary = dict({key:value})
        return newDictionary
    
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
    
    #identifies if coordinates are vague
    def ambigLocCheck(self, flank, MainWindow):
        invalidFlanks = ['>', '<']
        if (any(x in flank for x in invalidFlanks)):
            ambigLocCheck = True
        else:
            ambigLocCheck = False
        return ambigLocCheck
        
    def determineRange(self, location1, location2, MainWindow): 
        minF1 = (min(location1))
        maxF1 = (max(location1))
        minF2 = (min(location2))
        maxF2 = (max(location2))
                    
        locusvals = [minF1, maxF1, minF2, maxF2]
        loc_max = (max(locusvals) + 1)
        loc_min = (min(locusvals))         
        return loc_min, loc_max

    #compares the translation listed on the annot. file w/ the extracted seq
    def seqComparison(self, annotTransl, manualTransl, MainWindow):
        seqDifference = False
        #subtract point for opening gap, -0.5 for extending it
        align = pairwise2.align.globalxs(annotTransl, manualTransl, -1, -0.5)
        for a in align:
            #print(format_alignment(*a))
            al1,al2, score, begin, end = a
        metric = float(score/(end-begin))
        if metric < 1.0:
            seqDifference = True
        return seqDifference

        
        
