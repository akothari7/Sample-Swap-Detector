import numpy as np
import pandas as pd

data = pd.read_csv("UDI_verif_snps_2samples.txt", sep="\t")
SAMPLE_NAME = pd.Series(data["SAMPLE_NAME"])
SAMPLE_NAME.sort_values(ascending=True)

df= data.sort_values(by=['SAMPLE_NAME'], ascending=True)

grouped = data.groupby(data["SAMPLE_NAME"])
sample1 = grouped.get_group("HI--1")
sample1 = sample1[["SAMPLE_NAME", "ADJUSTEDFREQUENCY", "AMPLICON_NAME"]]
sample1 = sample1.sort_values(by=['AMPLICON_NAME'], ascending=True)
sample1 = sample1.set_index(sample1["AMPLICON_NAME"])
print(sample1[["SAMPLE_NAME", "ADJUSTEDFREQUENCY"]])

grouped = data.groupby(data["SAMPLE_NAME"])
sample2 = grouped.get_group("LO--1")
sample2 = sample2[["SAMPLE_NAME", "ADJUSTEDFREQUENCY", "AMPLICON_NAME"]]
sample2 = sample2.sort_values(by=['AMPLICON_NAME'], ascending=True)
sample2 = sample2.set_index(sample2["AMPLICON_NAME"])
print(sample2[["SAMPLE_NAME", "ADJUSTEDFREQUENCY"]])

spearman = sample1["ADJUSTEDFREQUENCY"].corr(sample2["ADJUSTEDFREQUENCY"], method='spearman')
print(spearman)

pearson = sample1["ADJUSTEDFREQUENCY"].corr(sample2["ADJUSTEDFREQUENCY"], method='pearson')
print(pearson)

