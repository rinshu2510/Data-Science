import pandas as pd
import numpy as np

def times2(x):
    return x*x

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})

# print(df['col2'].unique())
# print(df['col2'].nunique())
# print(df['col2'].value_counts())

# print(df['col1'].apply(times2))
# print(df['col1'].apply(lambda x : x*x))
# print(df['col3'].apply(len))
# print(df['col3'].sum())

# print(df.sort_values(by='col2'))
# print(df.isnull())

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
df2 = pd.DataFrame(data)
print(df2)
print()
print(df2.pivot_table(values='D',index=['A','B'],columns=['C']))


