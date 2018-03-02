# -*- coding:utf-8 -*-

import matplotlib.pyplot as pl 
from matplotlib.ticker import MultipleLocator, FuncFormatter
# 与刻度定位和文本格式化相关的类都在 matplotlib.ticker模块中定义，程序从中
# 载入了下两个类：
	# MultipleLocator: 以指定的值的整数倍为刻度防止主、副刻度线。
	# FuncFormatter: 使用指定的函数计算刻度文本，它会将刻度值和刻度的序号
	# 作为数值传递给计算刻度文本的函数。程序中通过pi_formatter()计算出刻度值对应的刻度文本


import numpy as np 

x = np.arange(0, 4*np.pi,0.01)
y = np.sin(x)
pl.figure(figsize = (8,4))
pl.plot(x,y)

ax = pl.gca()

def pi_formatter(x,pos):
	m = np.round(x/ (np.pi/4))
	n = 4
	print "f",m,n
	while n!=1 and m%2==0: 
		m,n = m//2,n//2
	print "b",m,n
	if m == 0:
		return "0"
	if m == 1 and n == 1:
		return "$\pi$"
	if n == 1:
		return r"$%d \pi$" % m
	if m == 1:
		return r"$\frac{\pi}{%d}$" % n
	return r"$\frac{%d \pi}{%d}$" % (m,n)

pl.ylim(-1.5,1.5)
pl.xlim(0,np.max(x))

pl.subplots_adjust(bottom = 0.15)
pl.grid()

ax.xaxis.set_major_locator(MultipleLocator(np.pi/4))

ax.xaxis.set_major_formatter(FuncFormatter(pi_formatter))

ax.xaxis.set_minor_locator(MultipleLocator(np.pi/20))

for tick in ax.xaxis.get_major_ticks():
	tick.label1.set_fontsize(16)
pl.show()