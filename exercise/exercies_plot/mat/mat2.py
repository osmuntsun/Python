import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)
y1 = 2*x + 1
y2 = x**2

#用兩個figure製作圖表
# plt.figure()
# plt.plot(x,y1)

# plt.figure()
# plt.plot(x,y2)

#用一個figure製作圖表
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')


plt.show()
