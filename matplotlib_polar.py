# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 

theta = np.arange(0,2*np.pi, 0.02)

plt.subplot(121,polar = True)# polar = True 创建极座标子图
plt.plot(theta,1.6*np.ones_like(theta),linewidth = 2) # 也可使用polar()直接创建极座标子图并在其中绘制曲线
plt.plot(3*theta,theta/3,"--",linewidth = 2)

plt.subplot(122,polar = True)
plt.plot(theta,1.4*np.cos(5*theta),"--",linewidth = 2)
plt.plot(theta,1.8*np.cos(4*theta),linewidth = 2)

plt.rgrids(np.arange(0.5,2,0.5),angle = 45)# 设置同心栅格角度
plt.thetagrids([0,45]) # 设置放射线栅格角度

plt.show()