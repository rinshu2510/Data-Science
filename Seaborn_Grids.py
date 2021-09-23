import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# iris = sns.load_dataset('iris')
# print(iris.head())

# g = sns.PairGrid(iris)
# g.map(plt.scatter)
# g.map_diag(plt.hist)
# g.map_lower(sns.kdeplot)
# g.map_upper(plt.scatter)
# plt.tight_layout()

# f = sns.FacetGrid(tips,row='smoker',col='time',hue='sex')
# f.map(sns.histplot,'total_bill')
# f.map(plt.scatter,'total_bill','tip')
# plt.legend(loc=0)

j = sns.JointGrid(x='total_bill',y='tip',data=tips)
j.plot(plt.scatter,sns.histplot)
plt.show()
