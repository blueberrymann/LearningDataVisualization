import matplotlib.pyplot as plt

# 创建绘图对象
plt.figure(figsize=(16,9))

# 绘制一条红色的线型字符为“：”的水平直线
plt.axhline(y=2, ls=":", c="red")

# 绘制一条从最左侧到画面中心位置，颜色为红色，线型字符为“：”的水平直线
plt.axhline(y=1.5, xmax=0.5, ls=":", c="red")

# 绘制一条从画面中心位置到最右侧，颜色为红色，线型字符为“：”的水平直线
plt.axhline(y=2.5, xmin=0.5, ls=":", c="red")

# 绘制一条绿色的线型为“-”的垂直线
plt.axvline(x=2, ls="-", c="green")

# 绘制一条从最下侧到画面中心为止，颜色为绿色，线型字符为“-”的垂直线
plt.axvline(x=1.5,ymax=0.5,ls="-",c="green")

# 绘制一条从画面中心位置到最上侧，颜色为绿色，线型字符为“-”的垂直线
plt.axvline(x=2.5,ymin=0.5,ls="-",c="green")

# plt.savefig('beeline')
plt.show()