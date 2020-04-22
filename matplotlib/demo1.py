import matplotlib.pyplot as plt
import numpy as np

#从【-1，1】中等距取50个数作为x的取值
x = np.linspace(-1, 1, 50)
print(x)
y1 = 2*x + 1
y2 = 2**x + 1
#使用figure()函数重新申请一个figure对象
#注意，每次调用figure的时候都会重新申请一个figure对象
plt.figure()
#第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y1)

#第一个参数表示的是编号，第二个参数表示图表的长宽
plt.figure(num=3, figsize=(8,5))

#当我们需要在画板中绘制两条线的时候，可以使用正面的方法
plt.plot(x, y2)
plt.plot(x, y1, 'r-')
plt.show()

#必要方法，用于将设置好的figure对象显示出来
plt.show()