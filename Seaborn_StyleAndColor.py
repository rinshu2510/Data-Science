import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

sns.set_style('whitegrid')
plt.figure(figsize=(8,5))
sns.set_context(context='paper',font_scale=2)
sns.barplot(y='total_bill',x='sex',data=tips,palette='magma')
# sns.despine(left=True)
plt.tight_layout()
plt.show()
