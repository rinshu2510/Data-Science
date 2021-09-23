import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1,21).reshape(5,4),['A','B','C','D','E'],['F','G','H',"I"])
df2 = pd.DataFrame()
print(df)
print()
# print(df['G'])
# print(df[['G','H']])
# print(df.I) avoid this method of selection column bcoz fuction in df may overlap with the nmes of column
# create new column
# df['J'] = [21 , 22, 23 ,24 , 25]
# print(df)
# # removing column
# print(df.drop('F',axis=1))
# print(df)
# df.drop('F',axis = 1,inplace=True)#remove column F permanantly
# print(df)
# print(df.drop('E'))
# print(df)
# df.drop('E',inplace=True)#remove row E permanantly
# print(df)

# #selecting Row

# print(df.loc['E'])
# print(df.iloc[1])

# selecting row and column

print(df.loc['B','G'])
print(df.loc[['A','B'],['G','I']])

