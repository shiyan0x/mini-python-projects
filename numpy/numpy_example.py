import numpy as np

#create a numpy array
array = np.array([1,2,3,4,5,6])

#perform basic openration
print("array:", array)
print("Mean:", np.mean(array))
print("sum:", np.sum(array))

#create a 2d array
matrix = np.array ([[1,2,3],[4,5,6]])

#matrix operation
print("matrix:\n", matrix)
print("transpose:\n", np.transpose(matrix))
print("Element wise addition:\n", matrix + 10)