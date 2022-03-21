import matplotlib.pyplot as plt
import numpy as np
#設置坐標軸

x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

plt.figure(figsize=(10,5))
#XY範圍
plt.xlim((-1,2))
plt.ylim((-2,-3))

#XY描述
plt.xlabel('I AM X')
plt.ylabel('I AM Y')
new_ticks = np.linspace(-2,2,11)

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')

plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
            ['level','level2','level3','level4','level5'])

#獲取座標
ax = plt.gca()




plt.show()