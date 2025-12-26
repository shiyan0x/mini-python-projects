import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,2,30,4,60]

plt.fill_between(x,y, color='skyblue' , alpha = 0.6)
plt.grid(axis='y', linestyle=':', color='b', alpha=0.8)
plt.show()