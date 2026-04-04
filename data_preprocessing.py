# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OrdinalEncoder

#1. Loading the data
#Trying to read the housing csv file
try:
    data_path = './week04/housing.csv'
    my_housing = pd.read_csv(data_path)
except:
    #If the first path fails, try local directory
    my_housing = pd.read_csv('./housing.csv')

#2. Creating training and test sets
#I need to categorize income to split the data correctly
my_housing["income_cat"] = pd.cut(my_housing["median_income"],
                                  bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                  labels=[1, 2, 3, 4, 5])

#Stratified split to keep the same proportion of income categories
train_set, test_set = train_test_split(
    my_housing, test_size=0.2, stratify=my_housing["income_cat"], random_state=42)

#Removing the temp category column after splitting
for dataset in (train_set, test_set):
    dataset.drop("income_cat", axis=1, inplace=True)

#Separate features and labels for the model
#Features (X)
housing_features = train_set.drop("median_house_value", axis=1)
#Target Labels (y)
housing_target = train_set["median_house_value"].copy()


#3. Data Cleaning (Handling Missing Values)
#Checking which rows have null/NaN values
missing_data_rows = housing_features.isnull().any(axis=1)
print("Rows with missing values:")
print(housing_features.loc[missing_data_rows].head())

#Using SimpleImputer to fill gaps with the median value
my_imputer = SimpleImputer(strategy="median")

#We only work with numbers for the imputer
housing_only_nums = housing_features.select_dtypes(include=[np.number])

#Training the imputer
my_imputer.fit(housing_only_nums)

#Comparing imputer results with manual median calculation
print("Imputer stats:", my_imputer.statistics_)
print("Manual median:", housing_only_nums.median().values)

#Filling the missing values in the dataset
transformed_values = my_imputer.transform(housing_only_nums)

#Putting the data back into a clean DataFrame
housing_cleaned = pd.DataFrame(transformed_values, 
                               columns=housing_only_nums.columns,
                               index=housing_only_nums.index)


#4. Removing Outliers (Bad data points)
# Using Isolation Forest to find weird data
iso_forest = IsolationForest(random_state=42)
is_outlier = iso_forest.fit_predict(transformed_values)

#Keeping only the normal rows (where result is 1)
housing_final = housing_features.iloc[is_outlier == 1]
labels_final = housing_target.iloc[is_outlier == 1]


#5. Handling Text/Categorical columns
# Focus on the 'ocean_proximity' column
housing_category_col = housing_final[["ocean_proximity"]]

#Converting text categories into numbers (0, 1, 2...)
my_encoder = OrdinalEncoder()
encoded_categories = my_encoder.fit_transform(housing_category_col)

print("First 8 encoded categories:")
print(encoded_categories[:8])
print("Categories found by encoder:", my_encoder.categories_)

print("Pre-processing complete!")
