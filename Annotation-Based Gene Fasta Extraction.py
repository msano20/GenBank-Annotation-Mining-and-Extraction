"""
Python 3.7.6 
IPython 7.12.0 -- An enhanced Interactive Python.
Written with Spyder 4.0.1 (Anaconda Suite)
@author: Misumi Sano (msano01@qub.ac.uk)
"""

import os
import logging
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

logging.basicConfig(filename='Errors.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

#Customizable variables
flank1 = 'urease accessory protein UreG' #enter flanking gene product
flank2 = 'symmetrical bis(5\'-nucleosyl)-tetraphosphatase'
targetgene = 'ABC transporter ATP-binding protein' #enter target gene product
file_tag = "wzt" #this is just for file naming conventions
homolog_threshold = 2 #if the amount of found targets exceeds this integer, the file will be skipped
locusthresh = 65000 #Locus size threshold in base pairs


#Core script
for root, dirs, assembly in os.walk('.', topdown=True):
    for strain in assembly:
        strain = os.path.join(root, strain)
        if strain.endswith('.gbff'):
            ureg_loc = ''
            apah_loc = ''
            target_loc = ''
            print("Opening: ", strain)
            for record in SeqIO.parse(strain, "gb"):
                for feature in record.features:
                    if feature.type == "CDS":
                        if feature.qualifiers['product'][0] == flank1:
                            ureg_loc = feature.location
                            ureg_desc = record.description
                        if feature.qualifiers['product'][0] == flank2:
                            apah_loc = feature.location 
                            apah_desc = record.description
                            
            print("Flank1 Location: " + str(ureg_loc))
            print("Flank2 Location: " + str(apah_loc))
            
            #Establishing parameters to search within            
            try:
                miu = (min(ureg_loc))
                mau = (max(ureg_loc))
                mia = (min(apah_loc))
                maa = (max(apah_loc))
                    
                locusvals = [miu,mau,mia,maa]
                loc_max = (max(locusvals))
                loc_min = (min(locusvals))
                
            
            except:
                print("Error: Flank(s) could not be found")
                logging.error("%s : Flanks not found" % (record.description))
                continue
                
            if loc_max - loc_min > locusthresh:
                print("%s : Locus size exceeds %s " % (record.description, locusthresh))
                logging.error("%s: Locus size exceeds established threshold of %s" % (record.description, locusthresh))
                continue
                
            candidate = []
            for record in SeqIO.parse(strain, "gb"):
                for feature in record.features:
                    if record.description == ureg_desc == apah_desc:
                        if feature.type == "CDS":
                            if feature.qualifiers['product'][0] == targetgene and \
                                loc_min < min(feature.location) < loc_max:
                                candidate.append(feature) #append SeqFeature object
                                try:
                                    rec_desc = record.description
                                except:
                                    rec_desc = ""
                                try:
                                    rec_id = record.id
                                except:
                                    rec_desc = ""
                                print("Found: " + feature.qualifiers['product'][0])

                                
            if candidate != []:
                if len(candidate) <= homolog_threshold:
                    for item in candidate:
                        try:
                            protid = str(item.qualifiers['protein_id'])
                            raw_protid = protid.strip("[\']")
                        except:
                            raw_protid = str("WP_NaN")
                                        
                        try:
                            gene_seq = (item.qualifiers['translation'][0])
                            new_record = SeqRecord(Seq(gene_seq), id = rec_id, 
                                            description = raw_protid + " " + rec_desc)
                            SeqIO.write(new_record, rec_desc + "_" + file_tag + " " + "("
                                        + raw_protid + ")" + ".fasta", "fasta")
                            print("Sequence Extracted.")
                        except:
                            print("Translation unavailable")
                            logging.error("%s : No sequence available" % (record.description))
                            continue
            
                else:
                    print("Excess candidates detected: " + str(record.description))
                    print("Number of Candidates: " + str(len(candidate)))
                    print("Aborting.")
                    logging.error("%s : Homologs exceed established threshold:" % (record.description))
                    continue
            
            else:
                print("Candidates empty.")
                print("Aborting.")
                logging.error("%s : No potential candidates found" % (record.description))
                continue
            ureg_loc = None
            apah_loc = None

           


print("Done.")
