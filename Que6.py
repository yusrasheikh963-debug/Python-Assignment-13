import numpy as np

v1 = np.array([2, 4, 6, 8])   #Create vectors (1D arrays)
v2 = np.array([1, 3, 5, 7])

print("Addition:")   #Addition
print(v1 + v2)

print("\nSubtraction:")   #Subtraction
print(v1 - v2)

print("\nElement-wise Multiplication:")  #Element-wise Multiplication
print(v1 * v2)

print("\nDot Product:")   # Dot Product
print(np.dot(v1, v2))