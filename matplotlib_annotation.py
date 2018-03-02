# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties

def func1(x):
	return 0.6*x+0.3

def func2(x):
	return 0.4*x*x + 0.1*x +0.2

# 定义了两个函数

def find_curve_intersects(x,y1,y2):
	d = y1 - y2
	idx = np.where(d[:-1]*d[1:] <= 0)[0]
	x1,x2 = x[idx],x[idx+1]
	d1,d2 = d[idx],d[idx+1]
	return -d1*(x2 - x1)/(d2-d1) + x1

# 用该函数计算两条曲线的交点坐标

x = np.linspace(-3,3,100)
f1 = func1(x)
f2 = func2(x)
plt.figure(figsize = (8,4))
plt.plot(x,f1)
plt.plot(x,f2)

x1,x2 = find_curve_intersects(x,f1,f2)
#算出交点
plt.plot(x1,func1(x1),"o")
plt.plot(x2,func1(x2),"o")
#仍使用plot绘制坐标点

plt.fill_between(x,f1,f2,where = f1>f2,facecolor = "green",alpha = 0.5)
#绘制面积
from matplotlib import transforms
ax = plt.gca()
trans = transforms.blended_transform_factory(ax.transData,ax.transAxes)
plt.fill_between([x1,x2],0,1,transform = trans,alpha = 0.1)

#绘制矩形区


font = FontProperties(fname = r"/Library/Fonts/AdobeFangsongStd-Regular.otf")

a = plt.text(0.05,0.95,u"直线和二次曲线的交点",
	transform = ax.transAxes,
	verticalalignment = "top",
	fontsize = 18,
	bbox = {"facecolor":"red","alpha":0.4,"pad":10},
	fontproperties = font
)
#添加文字

arrow = {"arrowstyle":"fancy,tail_width = 0.6",
		"facecolor":"gray",
		"connectionstyle":"arc3,rad = -0.3"}

plt.annotate(u"交点",
			xy = (x1,func1(x1)),xycoords = "data",
			xytext = (0.05,0.5),textcoords = "axes fraction",
			arrowprops = arrow,
			fontproperties = font
			)
#添加箭头

plt.annotate(u"交点",
	xy = (x2,func1(x2)),xycoords = "data",
	xytext = (0.05,0.5),textcoords = "axes fraction",
	arrowprops = arrow,
	fontproperties = font)

xm = (x1+x2)/2
ym = (func1(xm) - func2(xm))/2 + func2(xm)

o = plt.annotate(u"直线大于曲线区域",
	xy = (xm,ym),xycoords = "data",
	xytext = (30,-30),textcoords = "offset points",
	bbox = {"boxstyle":"round","facecolor":(1.0,0.7,0.7),"edgecolor":"none"},
	fontsize = 16,
	arrowprops = {"arrowstyle":"->"},
	fontproperties = font
)

#plt.show()

print type(ax.transData)

print ax.transData.transform([(-3,-2),(3,5)])# 计算数据坐标系中的坐标点在绘图窗口中的坐标
print ax.transAxes.transform([(0,0),(1,1)]) # 计算子图坐标系在绘图窗口中的坐标
print plt.gcf().transFigure.transform([(0,0),(1,1)]) # 计算图表坐标系中坐标点在绘图窗口中的位置



