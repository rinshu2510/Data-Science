import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head( ))
# sns.distplot(tips['total_bill'],kde=False)
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')

# sns.pairplot(tips,hue='sex')
# sns.rugplot(tips['total_bill'])
sns.kdeplot(tips['total_bill'])
plt.show()