# -*- coding: utf-8 -*-
"""
Python 3.7.6 
IPython 7.12.0 -- An enhanced Interactive Python.
Written with Spyder 4.0.1 (Anaconda Suite)
@author: Misumi Sano (msano01@qub.ac.uk)
"""
import os
import logging
import csv
from Bio import SeqIO

logging.basicConfig(filename='Errors.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

target_gene = 'ABC transporter ATP-binding protein' #Enter the gene to be extracted between flanks. 

flank_1 = 'urease accessory protein UreG' #Enter flank
flank_2 = 'symmetrical bis(5\'-nucleosyl)-tetraphosphatase' #Enter flank

csv_headers = ['Species', 'Group', 'Strain', 'Chr', 'Accession', 'LocusTag', 'ProtID', 'Seq']

output_filename = "Gene_extraction.csv"

max_homologs = 2
locusthresh = 65000 #enter locus threshold size in base pairs


#Configurations for output csv file
with open(output_filename, 'w', newline='') as csvfile:  
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(csv_headers)
    csvfile.close()

for root, dirs, assembly in os.walk('.', topdown=True):
    
    for strain in assembly:
        strain = os.path.join(root, strain)
        if strain.endswith('.gbff'):
            print(strain)
            for record in SeqIO.parse(strain, "gb"):
                #print(record.features[0])
                #print(record.annotations["source"])
                for feature in record.features:
                    #print(feature.source)
                    if feature.type == "CDS":
                        if feature.qualifiers['product'][0] == flank_1:
                            ureg_loc = feature.location
                            ureg_desc = record.description
                        if feature.qualifiers['product'][0] == flank_2:
                            apah_loc = feature.location
                            apah_desc = record.description
            
            
            try:
                miu = (min(ureg_loc))
                mau = (max(ureg_loc))
                mia = (min(apah_loc))
                maa = (max(apah_loc))
                    
                locusvals = [miu,mau,mia,maa]
                loc_max = (max(locusvals))
                loc_min = (min(locusvals))
                
                print("Locus minimum:",loc_min)
                print("Locus maximum:",loc_max)
            except:
                print("flank not determined")
                logging.error('%s Flank locations could not be determined' % (strain))
                continue
                
            if loc_max - loc_min > locusthresh:
                print("%s : Locus size exceeds %s " % (record.description, locusthresh))
                logging.error("%s: Locus size exceeds established threshold of %s" % (record.description, locusthresh))
                continue    
            
            #search process
            candidate = [] #contains the gene of interest
            for record in SeqIO.parse(strain, "gb"):
                if record.description == ureg_desc == apah_desc:
                    gene_desc = record.description
                    print(gene_desc)
                    for feature in record.features:
                        if feature.type == "CDS":
                            if feature.qualifiers['product'][0] == target_gene and \
                            loc_min < min(feature.location) < loc_max: 
                                print(feature.qualifiers['product'][0])    
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
                                
                            
                            
            if candidate != []:
                if len(candidate) <= max_homologs:
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
                        #FIX!
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
                                    
                        try:
                            gene_seq = (item.qualifiers['translation'][0])
                        except:
                            logging.error('%s %s sequence information unavailable' % (gene_desc, strain))
                            gene_seq = float("NaN")

                        print(c_species, c_family, c_strain_raw, c_chr_raw, rec_id, c_locustag_raw, raw_protid, gene_seq)                  
                        new_row = [c_species, c_family, c_strain_raw, c_chr_raw, rec_id, c_locustag_raw, raw_protid, gene_seq]
                                
                        with open(output_filename, 'a', newline='') as csvfile:  
                            writer = csv.writer(csvfile)
                            writer.writerow(new_row)
                            csvfile.close()
                else:
                    print("multiple candidates match description")
                    logging.error('%s %s multiple candidates match description' % (gene_desc, strain))
                    continue
            else:
                print("No genes within locus fit the product description")
                logging.error('%s %s No genes within locus fit the product description' % (gene_desc, strain))
                continue
                                  
            ureg_loc = None
            apah_loc = None
                        

            
            
