import urllib
import pandas as pd
import os

def download_uniprots():
    df = pd.read_excel('fasta_to_uniprot.xlsx')

    id_list = [x for x in df['Uniprot_ID']]

    no_isoform_list = [x for x in id_list if '-' not in x]

    print(id_list)
    print(no_isoform_list)

    os.makedirs('XML', exist_ok=True)

    for i in no_isoform_list:
        urllib.request.urlretrieve('http://www.uniprot.org/uniprot/' + i + '.xml', 'XML/' + i + '.xml')

download_uniprots()
