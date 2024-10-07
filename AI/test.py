import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1,2],[3,4]])
b = np.array([10,20])

c = a*b
print(c)


#大于15的值
print(c[c>15])


x = np.arange(0, 6, 0.1) # 以0.1为单位，生成0到6的数据
y = np.sin(x)
plt.xlabel("x") # x轴标签
plt.ylabel("y") # y轴标签
plt.title('sin & cos') # 标题
plt.plot(x, y)
plt.show()




def sigmoid(x):
 return 1 / (1 + np.exp(-x))

def relu(x):
 return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.show()