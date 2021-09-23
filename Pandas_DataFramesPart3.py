import pandas as pd
import numpy as np

# multiIndex and Index Hierarchy
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)  # customisation of working on data frame
print(hier_index)

df = pd.DataFrame(np.random.rand(6,2),hier_index,['A','B'])
print(df)

print(df.loc['G1']['A'])

df.index.names = ['Group' , 'No']
print(df)

print(df.loc['G2'].loc[1,'B'])

print(df.xs(1,level='No'))