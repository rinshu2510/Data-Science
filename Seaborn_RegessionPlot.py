import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','1'],palette='magma')
# sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time',hue='sex').add_legend(loc=1)
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',aspect=1,height=5)
plt.tight_layout()
plt.show()