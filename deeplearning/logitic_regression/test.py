import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

y1_x1_mu,y1_x1_sigma = 0,2 #均值与标准差
y1_x2_mu,y1_x2_sigma = 3,3.5
y1_x1 = np.random.normal(y1_x1_mu,y1_x1_sigma,50)
y1_x2 = np.random.normal(y1_x2_mu,y1_x2_sigma,50)
y1 = np.ones((50,1))

y0_x1_mu,y0_x1_sigma = 0,1 #均值与标准差
y0_x2_mu,y0_x2_sigma = 10,3
y0_x1 = np.random.normal(y1_x1_mu,y1_x1_sigma,50)
y0_x2 = np.random.normal(y0_x2_mu,y0_x2_sigma,50)
y0 = np.zeros((50,1))

x1 = list(y1_x1)
x1.extend(list(y0_x1))

x2 = list(y1_x2)
x2.extend(list(y0_x2))

y = list(y1)
y.extend(list(y0))
#------保存数据 ------
with open("logisticData.txt","w") as f:#使用with不需要f.close()
    for i in range(100):
        write_str = '%f %f %d\n'%(x1[i],x2[i],y[i])
        f.write(write_str)
#------画出散点图  ------
line1,= plt.plot(x1[:50],x2[:50],'ro',label = 'class1')
line2, = plt.plot(x1[50:],x2[50:],'b^',label ='class0')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(handles=[line1,line2],loc = 2)
plt.show()
