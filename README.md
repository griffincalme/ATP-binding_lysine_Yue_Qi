# ATP-binding_lysine_Yue_Qi
Source code used in Yue Qi's dissertation


All files in the folder "XML" are as originally downloaded from uniprot.org and are redistributed under Creative Commons Attribution-NoDerivs License. http://www.uniprot.org/uniprot/?query=keyword:%22ATP-binding%20[KW-0067]%22&fil=organism%3A%22Homo+sapiens+%28Human%29+%5B9606%5D%22

## Download the .fasta file
Use the above link to obtain a .fasta file with all Human ATP-binding proteins

## fasta_to_excel.py
Parses out information from the fasta file and saves in an Excel spreadsheet

## download_uniprots.py
Takes the Excel spreadsheet and downloads individual XML files for each protein containing all of the information from each protein's webpage entry. The ATP binding site and region information will be extracted later.

## parse_individual_xml.py
Extracts information from each XML to determine which proteins have ATP-binding regions or sites and what the position in the sequence is.
Saves this information as `ATP_binding_sites.xlsx`

## has_lysine_in_site.py
Counts the number of lysines in each region or site.
Saves the final sheet as `ATP_binding_sites_complete.xlsx`
