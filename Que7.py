import numpy as np

# Create matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Addition of two matrix:")   # Matrix Addition
print(A + B)

print("\nMultiplication of two matrix:")   # Matrix Multiplication
print(A @ B)      # or np.dot(A, B)

print("\nElement-wise Multiplication:")   # Element-wise Multiplication
print(A * B)