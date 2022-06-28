import numpy as np
import pandas as pd

hi = True
data = pd.read_csv("UDI_verif_snps_2samples.txt", sep="\t")

df= data.sort_values(by=['SAMPLE_NAME'], ascending=True)
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
       print('\n' + "Here is the data for Sample " + str(i + 1))
       print my_vars['r' + str(i)]
       print('\n' + "Here is the data for Sample " + str(j + 1))
       print my_vars['r' + str(j)]
       pearson = my_vars['r'+str(i)].corrwith(my_vars['r'+str(j)], method='pearson')
       pearson = float(pearson)
       spearman = my_vars['r'+str(i)].corrwith(my_vars['r'+str(j)], method='spearman')
       spearman = float(spearman)

       print('\n' + "The spearman correlation coefficient of these two samples is " + str(spearman) + ".")
       print("The pearson correlation coefficient of these two samples is " + str(pearson) + ".")

       if spearman >= 0.75 and pearson >= 0.75:
           print('\n' + "These samples belong to the same patient.")

       elif spearman < 0.75 and pearson < 0.75:
           print('\n' + "These samples belong to different patients.")

       elif spearman >= 0.75 and pearson < 0.75:
           print('\n' + "According to the spearman coefficient, these samples belong to the same patient, but according to the pearson coefficient, they belong to different ones.")

       elif spearman < 0.75 and pearson >= 0.75:
           print('\n' + "According to the pearson coefficient, these samples belong to the same patient, but according to the spearman coefficient, they belong to different ones.")
