# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 

y,x = np.ogrid[-1.5:1.5:200j,-1.5:1.5:200j]
f = (x**2+y**2)**4 - (x**2-y**2)**2

plt.figure(figsize = (9,4))
plt.subplot(121)
extent = [np.min(x),np.max(x),np.min(y),np.max(y)]

cs = plt.contour(f,extent = extent,levels = [0,0.1],
	colors = ["b","r"],linestyles = ["solid","dashed"],linewidths = [2,2])

# 通过levels参数指定所绘制等值线对应的函数值。
# 通过其他参数指定颜色线型线宽

# 可以通过contour()返回的对象，即cs，获得等值线上每点的数据
# cs是一个QuadContourSet对象
print cs
# cd的collections属性是一个等值线列表，每条等值线用一个LineCollection对象表示
print cs.collections
# 每一个LineCollection对象都有它自己的颜色、线型、线宽等属性，
#但还有封装，需要获得其第0个元素才是真正的配置
print cs.collections[0].get_color()[0]
print cs.collections[0].get_linewidth()[0]
# 获得所有等值线的所有路径
print len(cs.collections[0].get_paths())

#路径是一个Path对象，通过它的vertices属性可以获得路径上所有的点的坐标
path = cs.collections[0].get_paths()[0]
print path.vertices

plt.subplot(122)
for c in cs.collections:
	data = c.get_paths()[0].vertices
	plt.plot(data[:,0],data[:,1],
		color = c.get_color()[0],linewidth = c.get_linewidth()[0])

plt.show()