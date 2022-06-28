import pandas as pd
import numpy as np

data = pd.read_csv("UDI_verif_snps_2samples.txt", sep="\t")

la = list(data['SAMPLE_NAME'].drop_duplicates())

cols = len(la)
rows = len(la)

mat = np.array([[0 for _ in range(cols)] for _ in range(rows)], dtype=np.float64)

my_vars=dict()
new_vars = dict()
for i in range(0, len(la)):
    grouped = data.groupby(data["SAMPLE_NAME"])
    my_vars['r'+str(i)] = grouped.get_group(la[i])
    my_vars['r'+str(i)] = my_vars['r'+str(i)].sort_values(by=['AMPLICON_NAME'], ascending=True)
    my_vars['r'+str(i)] = my_vars['r'+str(i)].set_index(my_vars['r'+str(i)]["AMPLICON_NAME"])
    my_vars['r' + str(i)] = my_vars['r' + str(i)][["ADJUSTEDFREQUENCY"]]
    my_vars['r' + str(i)].rename(columns = {"ADJUSTEDFREQUENCY": my_vars['r' + str(i)]})

for i in range(0, len(la)-1):
    for j in range(1, len(la)):
       print my_vars['r' + str(i)]
       print my_vars['r' + str(j)]
       correlation = my_vars['r'+str(i)].corrwith(my_vars['r'+str(j)], method='pearson')
       mat[i][j] = correlation

print mat