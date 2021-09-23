import pandas as pd

df = pd.read_csv('Ecommerce Purchases')

# print(df.head())
# print(df.info())

# print(df['Purchase Price'].mean())
# print(df['Purchase Price'].max())
# print(df['Purchase Price'].min())

# print(df[df['Language']=='en'].value_counts())
# print(df[df['Job']=='Lawyer']['Job'].value_counts())

# print(df.groupby('AM or PM')['AM or PM'].value_counts())

# print(df.groupby('Job')['Job'].describe().sort_values('count',ascending=False).head(5)['count'])

# print(df[df['Lot']=='90 WT']['Purchase Price'])

# print(df[df["Credit Card"]==4926535242672853]['Email'])

# print(df[(df['CC Provider']=='American Express') & (df['Purchase Price']>95)].count())

# print(sum(df['CC Exp Date'].apply(lambda x:x[3:]=='25')))
# print(df[df['CC Exp Date'].apply(lambda x:x[3:]=='25')].count())

print(df['Email'].apply(lambda email:email.split('@')[1]).value_counts().head(5))

