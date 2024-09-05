import pandas as pd

# 导入数据
df = pd.read_csv('./Files/china_population.csv',encoding='utf-8')
print(df)

# 获取2015-2019年的年份数据
df1 = df.iloc[5:1:-1]
year = list(df1)
print(df1)
print(year)

# 获取2015-2019年的Population, Median Age
df1 = df.iloc[5:1:-1,[1,5]]
print(df1)
data1 = list(df1.iloc[0])
print(data1)
