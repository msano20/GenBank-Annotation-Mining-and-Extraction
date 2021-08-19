# -*- coding: utf-8 -*-
"""
Python 3.7.6 
IPython 7.12.0 -- An enhanced Interactive Python.
Written with Spyder 4.0.1 (Anaconda Suite)
@author: Misumi Sano (msano01@qub.ac.uk)

"""


import os
import logging
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SearchIO

logging.basicConfig(filename='Errors.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

#Configurable variables
possiblefileexts = (".fasta", ".fna")  #add any other formats you want read
maxlocussize = 65000 #enter your cut-off size in base pairs for your OAG Locus 

flank1db = "apaHdb" #enter names for Blast DBs
flank2db = "ureGdb"

hspidentitymin = 400 #minimum identical bp alignments for flank search

#Core script
for root, dirs, fastaassembly in os.walk('.', topdown=True):
    for fastafile in fastaassembly:
        if 'Oantigenlocus' not in fastafile and fastafile.endswith(possiblefileexts):
            with open(fastafile,'r') as f:
                print("Opening:", fastafile)
            #Opens each fasta file and blasts for the flank
            #Make sure your flank DBs are in the same file. 
                #for flank1 database:
                flank1output = NcbiblastnCommandline(task='blastn', query = fastafile, db = flank1db, evalue = 0.05,
                                                out = os.path.splitext(fastafile)[0]+'_' + flank1db + '.xml', outfmt = 5,
                                                max_hsps = 1)
                stdout, stderr = flank1output()
            
                #for flank2 database:
                flank2output = NcbiblastnCommandline(task='blastn', query = fastafile, db = flank2db, evalue = 0.05,
                                                out = os.path.splitext(fastafile)[0]+ '_' + flank2db + '.xml', outfmt = 5,
                                                max_hsps = 1)
                stdout, stderr = flank2output()
            
                fileidentity_flank1 = (os.path.splitext(fastafile)[0]+'_' + flank1db + '.xml')
                fileidentity_flank2 = (os.path.splitext(fastafile)[0]+'_' + flank2db +'.xml')

                #flank1 extraction
                #searching flank1 iterations for highest bit score
                qresultflank1 = SearchIO.parse(fileidentity_flank1, 'blast-xml')
                evaltest = []
                for qresult in qresultflank1:
                    print(qresult.description)
                    for hit in qresult:
                        for hsp in hit:
                            evaltest.append(hsp.bitscore)
                            print('Bitscore:', hsp.bitscore)
                                
                                
                print("contents of eval test (apaH):",evaltest)
                winner = max(evaltest)
                print("highest score in eval test:",winner)
            
            #extracting flank1 query start+end and description
                qresultflank1 = SearchIO.parse(fileidentity_flank1, 'blast-xml')
                for qresult in qresultflank1:
                    for hit in qresult:
                        for hsp in hit:
                            if hsp.bitscore == winner:
                                if hsp.ident_num > hspidentitymin:
                                    for hspfrag in hsp:
                                        flank1pos = hspfrag.query_start
                                        aqt = hspfrag.query_end
                                        apahdescr = qresult.description
                                        apahid = qresult.id
                                        print(apahdescr,"(",winner,")")
                                    
            #searching ureg iterations for highest bit score
                qresultflank2 = SearchIO.parse(fileidentity_flank2, 'blast-xml')
                evaltest = []
                for qresult in qresultflank2:
                    for hit in qresult:
                        for hsp in hit:
                            evaltest.append(hsp.bitscore)
                            print('Bitscore:', hsp.bitscore)
                                
                print("contents of evaltest (ureG)", evaltest)                
                winner = max(evaltest)
                print("Highest score in eval test:", winner)
            
                #extracting ureg query start+end and description
                qresultflank2 = SearchIO.parse(fileidentity_flank2, 'blast-xml')
                for qresult in qresultflank2:
                        for hit in qresult:
                            for hsp in hit:
                                if hsp.bitscore == winner:
                                    if hsp.ident_num > hspidentitymin:
                                        for hspfrag in hsp:
                                            flank2pos = hspfrag.query_start
                                            uqt = hspfrag.query_end
                                            uregdescr = qresult.description
                                            uregid = qresult.id
                                            print(uregdescr,"(",winner,")")
            
                #calculating bp range to extract
                qsep = {flank1pos, aqt, flank2pos, uqt}
                extractstart = min(qsep)
                extractend = max(qsep)
            
                if uregdescr == apahdescr:
                    print("Header matches")
                else:
                    logging.error("%s : Header descriptions don't match" % (fastafile))
                    continue
            
                print('Extracting between', extractstart,'and', extractend,"(",extractend-extractstart, "bp",")")
            
                #excessive BP troubleshooting
                deleteBP = extractend-extractstart #used for testing
                if extractend-extractstart > maxlocussize:
                    print("BP > 65kb. Skipping...")
                    logging.error("%s : Locus size exceeds maximum threshold" % (fastafile))
                    continue
                
                #writing
                if apahdescr == uregdescr:
                    oagfileidentity = ((os.path.splitext(fastafile)[0]) + '_Oantigenlocus' + '.fasta')
                    #for forward sequence
                    queryseq = open(fastafile,'r')
                    rs = open(oagfileidentity, 'w') #destination file for future handling
                    for record in SeqIO.parse(queryseq, 'fasta'):
                        if apahdescr in record.description:
                            newrecord = SeqRecord((record.seq[(extractstart):(extractend)]), id= uregid,
                                              description = uregdescr)
                            output_oa = SeqIO.write(newrecord,rs,"fasta")
            

                    #Reverse compl. the seq if apaH comes first
                            if flank2pos > flank1pos:
                                print("Minus strand. Reverse complementing...")
                                with open(oagfileidentity) as handle:  
                                    for rev in SeqIO.parse(oagfileidentity,'fasta'):
                                        rf_rev = rev.reverse_complement(id=(os.path.splitext(fastafile)[0]))
                                        newrecordplus = SeqRecord(rf_rev.seq, id=uregid,
                                                              description = uregdescr)
                                    
                                        #oagplusfileidentity = (os.path.splitext(fastafile)[0] + '_Oantigenlocus' + 'Plus strand' + '.fasta') ##!!!!!
                                        revresult = open(oagfileidentity, 'w')
                                        output_oa = SeqIO.write(newrecordplus,revresult,'fasta')
                                        
                else:
                    print("Headers for flank hits do not match.") 
                    logging.error("%s : FLank headers don't match" % (fastafile))
                
                del flank1output, flank2output, evaltest, winner, qsep, uregdescr, apahdescr, oagfileidentity
                print("Done.")
                

            
                                
            
            
                        
