# -*- coding:utf-8 -*-

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt 
import numpy as np 

font = FontProperties(fname = r"/Library/Fonts/AdobeFangsongStd-Regular.otf",size = 14)
# 创建描述字体属性的FontProperties对象，设置其fname属性为字体文件的绝对路径

t = np.linspace(0,10,1000)
y = np.sin(t)
plt.plot(t,y)
plt.xlabel(u"时间",fontproperties = font)
# 通过fontproperties参数讲FontProperties对象传递给显示文字的函数
plt.ylabel(u"振幅",fontproperties = font)
plt.title(u"正弦波",fontproperties = font)
plt.show()