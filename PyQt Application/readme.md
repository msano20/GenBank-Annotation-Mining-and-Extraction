This application was created using Qt verion 5.12.11 and Qt Creator version 4.15.1

## Usage
The purpose of this UI is to facilitate users who seek to mine data provided in NCBI annotation files. 
Annotation files must be in the standard .GBFF format. Collect all files to be extracted into a single folder and input it into the labeled field. The output will be a .CSV file stored in the same folder as your input.  
Flanks can be specified using the provided field inputs:
* product
* protein_id
* locus_tag

The program will accept mixed flank formats. It is recommended the flank identifiers used are unique. If more than two total flanks are found, the program will abort. 

Along with flank inputs, you can also specify a certain attribute within your target area in the form of the following specifiers:
* locus_tag
* old_locus_tag
* product
* protein_id

Note that if you enter multiple specifiers only CDS regions matching all of the provided fields will be returned. 

This program is intended for highly conserved flanks.

