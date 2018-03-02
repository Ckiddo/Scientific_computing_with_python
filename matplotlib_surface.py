# -*- coding:utf-8 -*-

import numpy as np 
import mpl_toolkits.mplot3d
# 载入mplot3d模块，由于绘制三维曲面的函数要求X、Y、Z的数据都使用
# 的相同形状的二维数组表示
import matplotlib.pyplot as plt 

x, y = np.mgrid[-2:2:20j,-2:2:20j]
z = x* np.exp(-x**2 - y**2)

ax = plt.subplot(111,projection = '3d')
# 创建子图，projection参数指定子图的投影模式为3d
# 投影模式:
# from matplotlib import projections
# projections.get_projection_names()
# 获取所有3d投影模式的
ax.plot_surface(x,y,z,rstride = 2,cstride = 1,cmap = plt.cm.Blues_r)

plt.show()