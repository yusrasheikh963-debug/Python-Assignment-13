import numpy as np 

arr = np.random.randint(1, 51, 20)   #Generate a 1D array of 20 random integers between 1 and 50

matrix = arr.reshape(4, 5)    #Reshape it into a 4x5 matrix
print("1D Array:")   # Print original 1D array
print(arr)

print("\n4x5 Matrix:")    # Print reshaped matrix
print(matrix)

print("\nSum of Matrix:", np.sum(matrix))    # Sum of all elements
print("Mean of Matrix:", np.mean(matrix))   # Mean of all elements

print("Standard Deviation of Matrix:", np.std(matrix))   # Standard deviation of all elements   

print("\nMaximum value in each row:")   # Maximum value in each row
print(np.max(matrix, axis=1))