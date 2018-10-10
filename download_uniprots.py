import urllib
import pandas as pd

df = pd.read_excel('../HUMAN_ATP_BINDING_Canon_Iso.fastauniprot.xlsx')



id_list = [x for x in df['Uniprot_ID']]



no_isoform_list = [x for x in id_list if '-' not in x]

print(id_list)
print(no_isoform_list)

for i in no_isoform_list:
    urllib.request.urlretrieve('http://www.uniprot.org/uniprot/' + i + '.xml', i + '.xml')


