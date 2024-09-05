import numpy as np
import matplotlib.pyplot as plt
# 在[0, 10]之间等距取1000个数作为x的取值
x = np.linspace(0,10,1000)
y = np.sin(x)

plt.figure(figsize=(16,9))
plt.plot(x,y,color="red",linewidth=3)

plt.title("AC Voltage")
plt.xlabel("Times(s)")
plt.ylabel("Volt")
plt.ylim(-1.5,1.5)
plt.xlim(0,10)

# 设置x轴刻度
ticks = [2, 4, 6, 8, 10]
labels = []