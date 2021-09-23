import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(1,21).reshape(5,4),['A','B','C','D','E'],['F','G','H','I'])
print(df)


#Conditional Selection
# print(df[df>10])
#
# print(df['F']>12)

# Give only rows where condition happens to be true
# print(df[df['F']>12])
# print(df[df['I']<5])

#single line selecting specific data satisfying the condition

print(df[df['F']!=9][['G','H']])
# Multiple condition

# print(df[(df['F']>4) & (df['F']<16)])

#resetting Index

# print(df.reset_index())
#
# print(df.set_index('I'))
