import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

tc = tips.corr()
# sns.heatmap(tc,cmap='Blues',linewidths=2,linecolor='white',annot=True)

sns.clustermap(tc)
plt.tight_layout()
plt.show()