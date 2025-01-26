# Day 6: Probability and Statistics FundamentalsCode: Write a program to calculate mean, median, mode, and variance of a dataset.

import numpy as np
from scipy import stats

# Sample dataset
data = [10, 20, 20, 30, 40, 50, 50, 50, 60]

# Mean
mean_value = np.mean(data)
print(f"Mean: {mean_value}")

# Median
median_value = np.median(data)
print(f"Median: {median_value}")

# Mode
mode_value, mode_count = stats.mode(data, keepdims=True)
print(f"Mode: {mode_value[0]} (Frequency: {mode_count[0]})")

# Variance
variance_value = np.var(data, ddof=1)  # Use ddof=1 for sample variance
print(f"Variance: {variance_value}")
