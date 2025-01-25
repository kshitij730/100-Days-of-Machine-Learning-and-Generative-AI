# Day 5: Linear Algebra Basics: Vectors and MatricesCode: Perform matrix operations like addition, multiplication, and inversion using NumPy

import numpy as np

# Define matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Addition of matrices
matrix_sum = matrix_a + matrix_b
print("Matrix Addition:")
print(matrix_sum)

# Multiplication of matrices
matrix_product = np.dot(matrix_a, matrix_b)
print("\nMatrix Multiplication:")
print(matrix_product)

# Element-wise multiplication
element_wise_product = matrix_a * matrix_b
print("\nElement-wise Multiplication:")
print(element_wise_product)

# Inversion of a matrix
try:
    matrix_inverse = np.linalg.inv(matrix_a)
    print("\nMatrix Inversion:")
    print(matrix_inverse)
except np.linalg.LinAlgError:
    print("\nMatrix A is not invertible.")

# Transpose of a matrix
matrix_transpose = matrix_a.T
print("\nMatrix Transpose:")
print(matrix_transpose)

# Determinant of a matrix
matrix_determinant = np.linalg.det(matrix_a)
print("\nMatrix Determinant:")
print(matrix_determinant)
