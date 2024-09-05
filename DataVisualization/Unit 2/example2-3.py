import pandas as pd

# 从csv文件中读取文件内容
df = pd.read_csv('./Files/CoachList.csv',encoding='utf-8')
print(df)

# 一个实例
df1 = pd.read_csv('./Files/covid19_tweets.csv')
for item in range(10):
    print(df1.iloc[item])