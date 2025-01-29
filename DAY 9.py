# Data Preprocessing: Handling Missing Data and EncodingCode: Clean and preprocess a dataset with missing values and categorical data

import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load Titanic dataset
df = sns.load_dataset('titanic')
print("Original Dataset:")
print(df.head())

# Selecting relevant columns
df = df[['sex', 'age', 'embark_town', 'fare', 'class']]

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
