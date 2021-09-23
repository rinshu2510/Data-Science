import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10 , 'b':20 , 'c':30}

# print(pd.Series(data=my_data))
# OR
print(pd.Series(my_data))
print(pd.Series(my_data,labels))
print(d)
print(pd.Series(d))
ser1 = pd.Series([1,2,3,4],['India','USA','UK','France'])
# print(ser1['France'])
print()
ser2 = pd.Series([1,3,5,8,10],['India','USA','Italy','UK','France'])
print(ser1+ser2)

