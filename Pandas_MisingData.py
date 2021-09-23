import pandas as pd
import numpy as np

# Missing Data

d = {'A':[1,2,np.NAN],'B':[5,np.NAN,np.NAN],'C':[1,2,3]}

df = pd.DataFrame(d)
print(df)

# dropna()
print(df.dropna())

print(df.dropna(axis=1))

print(df.dropna(axis=1,thresh=2))

#fillna()

print(df.fillna(value=10))
print(df['B'].fillna(value = 10))
print(df.loc[[2],['B']].fillna(value=10))
print(df)
