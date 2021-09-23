import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('dark_background')
plt.style.use('ggplot')

df1 = pd.read_csv('df1',index_col=0)
df2 = pd.read_csv('df2')
print(df1.head())
print(df2.head())

# df1['A'].plot.hist(bins=50)
# df1.plot.hist()

# df2.plot.area(alpha=0.4)

# df2.plot.bar(stacked=True)
# df2.plot.line(x=df2.index,y='a',figsize=(12,3),lw=

# df1.plot.scatter(x='A',y='B')
# df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm',figsize=(8,4))
# df1.plot.scatter(x='A',y='B',s=df1['C']*200)

# df1.plot.hexbin(x="A",y='B',gridsize=35)

df1['A'].plot.kde()
df1.plot.kde()
plt.show()

