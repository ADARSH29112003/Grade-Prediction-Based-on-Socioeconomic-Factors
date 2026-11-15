import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV datesheet
df = pd.read_csv("student_grade_ses_dataset.csv")
print(df)

# Check the dataset's size show that wise we use shape attributes provide by pandas
# print("Dataset Shape: ",df.shape)

# Check Column Names because we need to know what information our dataset contain before analysis
print("Column Names: ", df.columns)

# Check the datatypes of columns 
print("Column Data Types: ")
print(df.dtypes)

# Display the First 5 Rows
print("First 5 rows: ")
print(df.head())

# Display the Last 5 Rows - Now we want to inspect the last five records to check whether the dataset is structured consistently from beginning to end

print("last 5 rows: ")
print(df.tail())

# Get Dataset Information 
# We done almost everything and know it but we still don't know how many non-missing values each column contains that's why we use "info()"

print("Dataset Information")
df.info()

# Identify Missing Values
# Imagine a student record where the family income or attendance rate is missing.

# If we perform calculations without checking missing values, our analysis may become inaccurate or incomplete.

# That's why we need to identify missing values before cleaning the dataset.

print("Missing Values in each column: ")
print(df.isnull().sum())

# Calculate Missing Value Percentage
print("Missing value Percentage: ")
print((df.isnull().sum() / len(df)) * 100)

# Identify Duplicate Rows
# Imagine the same student's complete record appears twice in our dataset.

# If we analyse both records, that student may be counted twice, potentially affecting our results.

# Therefore, we need to identify duplicate records before cleaning.
# PANDAS PROVIDES THE "DUPLICATED()" FUNCTION

print("Total Duplicate Rows: ")
print(df.duplicated().sum())

# Identify Duplicate Student IDs
# Now we'll use the subset parameter to check only a particular column. 

print("Duplicate Student ID: ")
print(df.duplicated(subset=["student_id"]).sum())

# Final Verification of Duplicate Records
print("Are all duplicated rows and student_id are same: ")
print(df.duplicated(subset=["student_id"]).equals(df.duplicated()))

# Data Cleaning TIme
# 
# 
# TO prevent are original datesheet we copy the records so for these pandas provides us copy() method  of a dataframe
cleaned_df = df.copy()
print("Original Dataset Shape: ", df.shape)
print("Duplicate Dataset Shape: ", cleaned_df.shape)

# Remove Duplicate Rows - If we keep them, the same student records may be counted more than once, which can affect our statistical analysis.

cleaned_df = cleaned_df.drop_duplicates()
print("Shape after Removing Duplicates: ", cleaned_df.shape)
print("Remaining Duplicate Rows: ", cleaned_df.duplicated().sum())

# Identify Missing Values in the Cleaned Dataset - Because our cleaning decisions must be based on the dataset we're actually analysing: cleaned_df, not the original df.

print("Missing Values after Removing Duplicates: ")
print(cleaned_df.isnull().sum())

# Calculate Median Values - We need to calculate the median of four numerical columns before filling their missing values.

# Calculate Median Values
print("Median Annual Family Income: ")
print(cleaned_df["annual_family_income_inr"].median())

print("Median Distance to School: ")
print(cleaned_df["distance_to_school_km"].median())

print("Median Attendance Rate: ")
print(cleaned_df["attendance_rate_pct"].median())

print("Median Previous year Grade: ")
print(cleaned_df["previous_year_grade_pct"].median())

# Fill Missing Numerical Values
# Pandas provides the fillna() method to replace missing values. 

cleaned_df["annual_family_income_inr"] = cleaned_df["annual_family_income_inr"].fillna(350605.5)
cleaned_df["distance_to_school_km"] = cleaned_df["distance_to_school_km"].fillna(2.8)
cleaned_df["attendance_rate_pct"] = cleaned_df["attendance_rate_pct"].fillna(86.0)
cleaned_df["previous_year_grade_pct"] = cleaned_df["previous_year_grade_pct"].fillna(62.2)

print("Missing Numerical Values After Cleaning: ")
print(cleaned_df[["annual_family_income_inr", "distance_to_school_km", "attendance_rate_pct", "previous_year_grade_pct"]].isnull().sum())

# Fill missing father education values
cleaned_df["father_education_level"] = cleaned_df["father_education_level"].fillna("Unknown")
print("Missing Father's Education Values: ")
print(cleaned_df["father_education_level"].isnull().sum())
