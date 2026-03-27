import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([10,20,30,40,50])

plt.plot(x , y , marker='o', color='b')

plt.title('line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.grid(True)
plt.show()