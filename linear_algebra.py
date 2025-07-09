import numpy as np

# Question 1:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Sum
sum_vector = a + b
print(f"Sum of vectors a and b: {sum_vector}")
# Diff
diff_vector = a - b
print(f"Difference of vectors a and b: {diff_vector}")

# Question 2:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Sum
sum_matrix = A + B
print(f"Sum of matrices A and B: {sum_matrix}")
# Diff
diff_matrix = A - B
print(f"Difference of matrices A and B: {diff_matrix}")

# Question 3:
dot_product = np.dot(a, b)  # a&b are same as before
print(f"Dot product of vectors a and b: {dot_product}")

# Question 4:
A1 = np.array([[1, 2, 3], [4, 5, 6]])
B1 = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
product_matrix = np.dot(A1, B1)
print(f"Product of matrices A1 and B1: {product_matrix}")

# Question 5:
a1 = np.array([1, 1, 2])
magnitude = np.linalg.norm(a1)
print(f"Magnitude of vector a1: {magnitude}")

# Question 6:
transpose_matrix = A.T  # same matrix A
print(f"Transpose of matrix A: {transpose_matrix}")
