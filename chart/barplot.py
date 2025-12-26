import matplotlib.pyplot as plt

#data
categories = ['A', 'B', 'C', 'D']
values = [10,20,10,40]

#create a bar plot
#plt.bar(categories, values , color='skyblue')
plt.barh(categories, values , color='skyblue')

#grid
plt.grid(axis='y', linestyle = '--' , alpha= 0.4)

#title
plt.title('Bar plot')
plt.xlabel('categories')
plt.ylabel('values')

plt.show()