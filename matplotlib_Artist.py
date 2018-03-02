# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure()
ax = fig.add_subplot(111)
t = ax.scatter(np.random.rand(20),np.random.rand(20))

plt.show()
