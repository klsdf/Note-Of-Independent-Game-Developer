import numpy as np

def sigmoid(x):
 return 1 / (1 + np.exp(-x))

def relu(x):
 return np.maximum(0, x)

def softmax(a):
 c = np.max(a)
 exp_a = np.exp(a - c) # 防止溢出对策
 sum_exp_a = np.sum(exp_a)
 y = exp_a / sum_exp_a
 return y


def mean_squared_error(y, t):
 return 0.5 * np.sum((y-t)**2)


# 交叉熵
def cross_entropy_error(y, t):
 delta = 1e-7
 return -np.sum(t * np.log(y + delta))


# 查看产生的结果中预测正确的结果占比为多少
def accuracy(self, x, t):
    y = self.predict(x)
    y = np.argmax(y, axis=1)
    t = np.argmax(t, axis=1)
    accuracy = np.sum(y == t) / float(x.shape[0])
    return accuracy
 



x = np.array([1,2])
w1 = np.array([[0.1,0.4,0.3],[0.2,0.5,-0.1]])
b1=np.array([0.1,0.2,0.3])

hidden1 = sigmoid( np.dot(x, w1)+b1  )  #3个元素

w2=np.array([[0.2,-0.1],[0.1,0.3],[0.3,0.1]])  #3列
b2=np.array([0.3,0.2])

hidden2  = sigmoid( np.dot(hidden1, w2)+b2  ) #2个元素
w3 = np.array([[0.2,-0.1],[0.1,0.3]])  
b3 = np.array([0.1,0.3])  

output = softmax( np.dot(hidden2, w3)+b2  ) 

print(output)



def numerical_diff(f, x):
 h = 1e-4 #0.0001
 return (f(x+h) - f(x-h)) / (2*h)