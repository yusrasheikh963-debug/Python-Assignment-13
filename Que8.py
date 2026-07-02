import numpy as np 

arr = np.random.randint(1, 101, (4, 4))   #Create a 4*4 matrix with random integers between 1 & 100

print("Matrix:")   # Print the matrix
print(arr)

print("\nShape of Matrix:", arr.shape)   #Shape gives no. of rows & columns
print("Dimension of Matrix:", arr.ndim)   # ndim gives number of dimensions
print("Size of Matrix:", arr.size)   # size gives total number of elements in matrix

print("Data Type:", arr.dtype)   # dtype shows data type of elements
print("Minimum Value:", arr.min())   # min() returns smallest element in matrix
print("Maximum Value:", arr.max())   # max() returns largest element in matrix