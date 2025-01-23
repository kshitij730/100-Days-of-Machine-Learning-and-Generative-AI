# Python Libraries for ML: NumPy and Pandas Basics
import pandas as pd
import numpy as np

# 1. Load a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", None],
    "Age": [24, 27, np.nan, 22, 25],
    "Salary": [50000, 54000, 58000, None, 52000],
    "Department": ["HR", "Finance", "IT", "Marketing", "Finance"]
}
df = pd.DataFrame(data)
print("Original Dataset:\n", df)

# 2. Clean the dataset
# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill missing Age with the mean
df['Salary'].fillna(df['Salary'].median(), inplace=True)  # Fill missing Salary with the median
df.dropna(subset=['Name'], inplace=True)  # Drop rows where Name is missing

# Rename columns
df.rename(columns={"Salary": "Annual_Salary", "Department": "Dept"}, inplace=True)

print("\nCleaned Dataset:\n", df)

# 3. Perform basic statistical operations
print("\nBasic Statistics:")
print("Mean Age:", df['Age'].mean())
print("Median Salary:", df['Annual_Salary'].median())
print("Total Salary:", df['Annual_Salary'].sum())

# 4. Element-wise operations using NumPy
salary_array = df['Annual_Salary'].to_numpy()
bonus_array = salary_array * 0.10  # Calculate a 10% bonus
total_salary_array = salary_array + bonus_array

print("\nElement-wise Operations with NumPy:")
print("Salaries:", salary_array)
print("Bonuses (10%):", bonus_array)
print("Total Compensation:", total_salary_array)

# 5. Matrix manipulations using NumPy
matrix = np.array([[2, 4], [6, 8]])
print("\nOriginal Matrix:\n", matrix)
print("Transposed Matrix:\n", matrix.T)
print("Element-wise Multiplication:\n", matrix * 2)
print("Matrix Dot Product:\n", np.dot(matrix, matrix))
