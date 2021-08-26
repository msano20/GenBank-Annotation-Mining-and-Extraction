This application was created using Qt verion 5.12.3 and PyQt Creator version 4.15.1

## Usage
The purpose of this UI is to provide a user-friendly tool to facilitate researchers who seek to efficiently mine data provided in NCBI annotation files across many different bacterial genomes.  The user will need to provide a specific region within the genome to scan which will be denoted by two conserved flanking genes or CDS regions. 
Annotation files must be in the standard .GBFF format. Collect all files to be extracted into a single folder and input it into the labeled field. Other files can be in the folder, but the program will only scan .GBFF files. The output will be a .CSV file stored in the same folder as your input.  This program has never been tested on eukaryotic genomes.

At present, the output contains the following headers:
* **Species**
* **Group**
* **Strain**
* **Chr**
* **Accession**
* **LocusTag**
* **ProtID**
* **Seq** (Amino acid. Does not include stop codon.)
* **Product**
* **Start** (using NCBI's 1-based indexing)
* **End** (1-based indexing)
* **Strand**
* **SeqOverride** (Extracts nucleotide sequence based on positioning, translates, and confirms the provided amino acid sequence. If the sequence extracted differs from the annotation-provided sequence, the manually translated sequence will take prececdence and this value will be set to True.  

Flanks can be specified using the provided field inputs:
* product
* protein_id
* locus_tag

The program will accept mixed flank formats. It is recommended the flank identifiers used are unique. If more than two total flanks are found, the program will not extract from that file. It is recommended to search based on locus_tag if only analyzing one file, and product if you are scanning many annotation files.

Along with flank inputs, you can also specify a certain attribute you are seeking within your target area in the form of the following specifiers:
* locus_tag
* old_locus_tag
* product
* protein_id

Note that if you enter multiple specifiers only CDS regions matching all of the provided fields will be returned. 

## Error Log
The program includes a basic error log configuration which will inform the user of various common errors encountered during extraction. They are as follows: 
* Ambiguous or joined sequence coordinates inputted as flanks. The script requires exact coordinates to know where to extract. 
* One or more inputted flank IDs could not be found within the file. 
* Multiple CDS regions in the file match one or more of the inputted flanks. Each flank must be unique so the script can know where to extract.
* Range could not be extracted from flank coordinates. 
* No genes could be found within the target region that match the provided identifiers. 


