import pandas as pd
# DataFrame是由多个Series组成的，当对应元素不存在的时候，pandas使用NaN进行补全
dt = {
    'product':pd.Series(['TV','Air Conditioner','Cleaner','PC'],index=['1','2','3','4']),
    'price':pd.Series([2300,1234,921],index=['1','2','3'])
}
# 不要显示定义index，应该定义组成DataFrame的Series的index
df = pd.DataFrame(dt)
print(df)

# 利用一个小实例来实践获取数据操作
df1 = pd.read_csv('./Files/covid19_tweets.csv')

# 输出所有列的名称和索引列表（输出行头和列头）
print(df1.columns) # 输出列头
print(df1.index) # 输出行头

# 选择所有元素
print('\n')
print(df1.values)


# 选择一列元素
print('\n')
print(df1['user_name'])

# 选择一行元素
print('\n')
print(df1.iloc[0])

# 选择多行元素
print('\n')
print(df1.iloc[0:2])

# 筛选元素
print('\n')
print(df1[df1['user_friends']>400000])