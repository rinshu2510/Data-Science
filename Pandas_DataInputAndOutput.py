import pandas as pd

#read and write CSV files

# print(pd.read_csv('ex.csv'))

# df = pd.read_csv('example')
# print(df)

# df.to_csv('Myoutput',index=False)
# print(pd.read_csv('Myoutput'))

# read and write excel file

df = pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')

print(df)
df.to_excel('MyOutput2.xlsx',sheet_name='NewSheet',index  = False)
print(pd.read_excel('MyOutput2.xlsx'))

