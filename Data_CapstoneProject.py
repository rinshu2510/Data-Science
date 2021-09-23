import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('911.csv')
# print(df.info())

print(df.head())
# print(df['zip'].value_counts().head(5))
# print(df['twp'].value_counts().head(5))
# print(df['title'].nunique())

df['Reason'] = df['title'].apply(lambda title : title.split(':')[0])
# print(df['Reason'].value_counts())

# sns.countplot(x=df['Reason'],data=df)
# plt.show()

# print(type(df['timeStamp'].iloc[0]))

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
time = df['timeStamp'].iloc[0]
# print(time.hour)
df['Hour'] = df['timeStamp'].apply(lambda time : time.hour)
df['Month'] = df['timeStamp'].apply(lambda time : time.month)
df['Day of week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
print(df['Day of week'].head())
