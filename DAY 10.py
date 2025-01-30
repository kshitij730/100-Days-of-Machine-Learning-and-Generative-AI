#Exploratory Data Analysis (EDA)Code: Generate summary statistics and visualize distributions for a dataset.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load Titanic dataset
df = sns.load_dataset('titanic')
print("Original Dataset:")
print(df.head())

# Selecting relevant columns
df = df[['sex', 'age', 'embark_town', 'fare', 'class']]

# Exploratory Data Analysis (EDA)
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Visualizing distributions
plt.figure(figsize=(10, 6))
sns.histplot(df['age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='class', y='fare', data=df)
plt.title('Fare Distribution by Class')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='sex', data=df)
plt.title('Gender Distribution')
plt.show()

# Handling missing values
imputer_numeric = SimpleImputer(strategy='mean')  # Replace missing values with mean
imputer_categorical = SimpleImputer(strategy='most_frequent')  # Replace with most frequent value

df['age'] = imputer_numeric.fit_transform(df[['age']])
df['embark_town'] = imputer_categorical.fit_transform(df[['embark_town']])

print("\nDataset after handling missing values:")
print(df.head())

# Encoding categorical data
label_encoder = LabelEncoder()
df['sex'] = label_encoder.fit_transform(df['sex'])

one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')
class_encoded = one_hot_encoder.fit_transform(df[['class']])
class_df = pd.DataFrame(class_encoded, columns=one_hot_encoder.get_feature_names_out(['class']))

df = pd.concat([df, class_df], axis=1).drop(columns=['class'])

print("\nDataset after encoding categorical data:")
print(df.head())
