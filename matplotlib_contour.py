# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 

y,x = np.ogrid[-2:2:200j,-3:3:300j] # 使得z的形状为(200,300)
z = x*np.exp(-x**2-y**2)

extent = [np.min(x),np.max(x),np.min(y),np.max(y)]

plt.figure(figsize = (10,4))
plt.subplot(121)
cs = plt.contour(z,10,extent = extent) #取值范围分为了10个区域
# contour返回一个QuadContourSet对象传递给calbel()为其中的等值线标上对应的值
plt.clabel(cs)

plt.subplot(122)
plt.contourf(x.reshape(-1),y.reshape(-1),z,20) #另一种传参方式


plt.show()

