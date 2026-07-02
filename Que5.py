import numpy as np

a = np.random.rand(10)    #1D array of 10 random numbers between 0 & 1
print("1D Array of 10 Random Numbers (0 to 1):")
print(a)

b = np.random.randn(3, 3)   #3*3 matrix of random numbers
print("\n3x3 Matrix of Random Numbers from Standard Normal Distribution:")
print(b)

c = np.random.randint(10, 51, (4, 5))     #4*5 array of random integers between 10 & 50
print("\n4*5 Array of Random Integers (10 to 50):")
print(c)