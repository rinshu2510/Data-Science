import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# sns.barplot(x= 'sex', y='total_bill',data=tips,estimator=np.std)
# sns.countplot(x='sex',data=tips)
# sns.boxplot(x='day',y='total_bill',data=tips,hue='sex',palette='rainbow')
# sns.violinplot(x='day',y='total_bill',data=tips)
# sns.stripplot(x='day',y='total_bill',data=tips,hue='sex', dodge=True)
# sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
sns.catplot(x='day', y='total_bill',data = tips,kind='violin')#most general plot
plt.tight_layout()
plt.show()

