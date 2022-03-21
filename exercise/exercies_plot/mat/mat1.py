import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,100)#從-1到1生成100個點
y = 2*x + 1
plt.plot(x,y)
plt.show()