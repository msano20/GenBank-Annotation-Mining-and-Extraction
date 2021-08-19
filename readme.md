This repository holds various tool I have created for the purpose of sequence extraction pertaining to exploration of O-polysaccharide synthesis and export within the Burkholderia genome. Bacterial genomes exhibit a greater degree of dynamicism and flexibility than eukaryotic genomes due to factors such as lateral gene transfer and environmental uptake. My approach relies on the conserved presence of recognized flanking genes that surround fluid gene sequences (such as those found in polysaccharide synthesis). In Burkholderia, the locus related to O-antigen transport is contained within the flanking genes UreG and ApaH, which is why you'll see references to these genes in some of these scripts.

I have aspired for this project to eventually become applicable to a broader range of bacterial genera, though this possibility will vary based on a microbe-by-microbe basis. My PyQt application is my latest approach to this. 

##### PyQt Application/
Employ conserved flanks in the form of locus tags, protein products, or protein IDs and extract specific genes (or the entire set of genes) located beteween. Further identifiers for desired genes can be entered in the supplied fields. Consult the readme contained in the subfolder for further information. 

##### Annotation-Based_Gene_Fasta_Extraction.py
Iterates through annotation (.GBFF) files, searches between flanks, and extracts target gene sequence. Outputs a .FASTA file.

##### Blast-Based_OAG_Extraction.py
Input a whole genome .FASTA file to receive the locus sequence in between as specified by two flanking genes.

##### CSV_Database_Creator.py
The original script I based the PyQt application on. Iterates through annotation (.GBFF) files, searches between flanks, and 
extracts a target gene sequence along with species, group, strain, chromosome, accession number, locus tag, and protein ID organized as fields within a CSV file.
