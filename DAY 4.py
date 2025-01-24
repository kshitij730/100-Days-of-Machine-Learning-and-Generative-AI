#  Visualize a dataset with histograms, bar charts, and scatter plots

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 33],
    'Scores': [3.5, 4.7, 2.9, 3.3, 4.1],
    'Age': [25, 40, 35, 60, 50]
}
df = pd.DataFrame(data)

# Histogram: Distribution of 'Values'
plt.figure(figsize=(10, 6))
plt.hist(df['Values'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Values', fontsize=14)
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Bar Chart: 'Category' vs 'Values'
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Values'], color='orange', alpha=0.8)
plt.title('Bar Chart: Category vs Values', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Scatter Plot: 'Scores' vs 'Age'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Scores', data=df, color='green', s=100)
plt.title('Scatter Plot: Scores vs Age', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Scores', fontsize=12)
plt.grid(linestyle='--', alpha=0.7)
plt.show()
