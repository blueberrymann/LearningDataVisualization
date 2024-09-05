import pandas as pd

# 声明一个Series对象
se1 = pd.Series([2, 3, 5, -7])
print(se1)

# 声明一个带指定index的Series对象
se2 = pd.Series([2, 3, 5, -7],index=['b','c','a','d'])
print(se2)

# 创建一个DataFrame对象
dt = {'name':['张燕','黎明','王勇'],
      'sex': ['False','True','True'],
      'age': [10, 20, 30]
}
df = pd.DataFrame(dt)
print(df)

# 只取部分列来创建DataFrame对象也是可以的
df1 = pd.DataFrame(dt,columns=['name','age'])
print(df1)

# 也可以手动设置DataFrame对象的index
df2 = pd.DataFrame(dt,index=['a','b','c'],columns=['name','age'])
print(df2)