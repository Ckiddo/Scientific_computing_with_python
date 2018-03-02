# -*- coding:utf-8 -*-

from matplotlib.font_manager import fontManager 
import matplotlib.pyplot as plt 
import os

fig = plt.figure(figsize = (12,6))
ax = fig.add_subplot(111)
plt.subplots_adjust(0,0,1,1,0,0)
plt.xticks([])
plt.yticks([])
x,y = 0.05,0.08
fonts = [font.name for font in fontManager.ttflist if 
	os.path.exists(font.fname) and os.stat(font.fname).st_size > 1e6]
#  利用os模块中的stat()获取字体文件的大小，并保留字体索引列表中大于1mb的所有字体文件。
font = set(fonts)
dy = (1.0-y)/(len(fonts)/4 + (len(fonts)%4 != 0))
for font in fonts:
	t = ax.text(x,y,u"中文字体",{'fontname':font,'fontsize':14},transform = ax.transAxes)
	# 调用子图对象的text()在其中添加文字。transform对应的值是字体名
	ax.text(x,y-dy/2,font,transform = ax.transAxes)
	x += 0.25
	if x >= 1.0:
		y += dy
		x = 0.05

plt.show()
