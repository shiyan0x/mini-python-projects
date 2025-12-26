import matplotlib.pyplot as plt

x = [1,7,3,4]
y = [10,20,5,30]

plt.scatter(x,y, color = 'skyblue' , marker='o')
plt.grid(True , alpha=0.4 , linestyle = '--')
plt.show()