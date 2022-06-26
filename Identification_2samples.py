import numpy as np
import pandas as pd

hi = True
data = pd.read_csv("UDI_verif_snps_2samples.txt", sep="\t")

df= data.sort_values(by=['SAMPLE_NAME'], ascending=True)

grouped = data.groupby(data["SAMPLE_NAME"])
sample1 = grouped.get_group("HI--1")
coverage1 = sum(sample1['ALL_READS'] > 500)
sample1 = sample1[["SAMPLE_NAME", "ADJUSTEDFREQUENCY", "AMPLICON_NAME"]]
sample1 = sample1.sort_values(by=['AMPLICON_NAME'], ascending=True)
sample1 = sample1.set_index(sample1["AMPLICON_NAME"])
print('\n' + "Here are the adjusted frequencies for the HI--1 sample")
print(sample1[["SAMPLE_NAME", "ADJUSTEDFREQUENCY"]])

grouped = data.groupby(data["SAMPLE_NAME"])
sample2 = grouped.get_group("LO--1")
coverage2 = sum(sample2['ALL_READS'] > 500)
sample2 = sample2[["SAMPLE_NAME", "ADJUSTEDFREQUENCY", "AMPLICON_NAME"]]
sample2 = sample2.sort_values(by=['AMPLICON_NAME'], ascending=True)
sample2 = sample2.set_index(sample2["AMPLICON_NAME"])
print('\n' + "Here are the adjusted frequencies for the LO--1 sample")
print(sample2[["SAMPLE_NAME", "ADJUSTEDFREQUENCY"]])

if coverage1 < 100 or coverage2 < 100:
    print("There are not enough qualifying SNP's in these samples to get accurate calculations.")
    exit()

spearman = sample1["ADJUSTEDFREQUENCY"].corr(sample2["ADJUSTEDFREQUENCY"], method='spearman')
print('\n' + "The spearman correlation coefficient of these two samples is " + str(spearman) + ".")

pearson = sample1["ADJUSTEDFREQUENCY"].corr(sample2["ADJUSTEDFREQUENCY"], method='pearson')
print("The pearson correlation coefficient of these two samples is " + str(pearson) + ".")

if spearman >= 0.75 and pearson >= 0.75:
    print('\n' + "These samples belong to the same patient.")

elif spearman < 0.75 and pearson < 0.75:
    print('\n' + "These samples belong to different patients.")

elif spearman >= 0.75 and pearson < 0.75:
    print('\n' + "According to the spearman coefficient, these samples belong to the same patient, but according to the pearson coefficient, they belong to different ones.")

elif spearman < 0.75 and pearson >= 0.75:
    print('\n' + "According to the pearson coefficient, these samples belong to the same patient, but according to the spearman coefficient, they belong to different ones.")

