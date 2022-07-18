import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("UDI_verif_snps_10samples.txt", sep="\t")

samples = data.groupby(["SAMPLE_NAME", "EXPERIMENT_NAME"])

df = pd.DataFrame()

for name, sample in samples:
    sample = sample.sort_values(by=['AMPLICON_NAME'], ascending=True)
    sample = sample.set_index("AMPLICON_NAME")
    coverage = sum(sample['ALL_READS'] > 500)
    if coverage >= 100:
        df[name] = sample["ADJUSTEDFREQUENCY"]

print df.astype(np.float64).corr("pearson")
sns.heatmap(df.astype(np.float64).corr("pearson"), annot = True, fmt='.2g',cmap= 'coolwarm')
plt.show()
