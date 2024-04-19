import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a Pandas DataFrame
file_path = r"C:\Users\shubh\Documents\Home\demo\train_data.csv"
loan_df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(loan_df.head())

# Summary statistics for numerical columns
numeric_columns = loan_df.select_dtypes(include=['number']).columns
print("\nSummary statistics of numerical columns:")
print(loan_df[numeric_columns].describe())

# Check for missing values
print("\nMissing values:")
print(loan_df.isnull().sum())

# Visualize distributions of numerical columns
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.histplot(loan_df['ApplicantIncome'], bins=20, kde=True)
plt.title('Distribution of Applicant Income')

plt.subplot(2, 2, 2)
sns.histplot(loan_df['CoapplicantIncome'], bins=20, kde=True)
plt.title('Distribution of Coapplicant Income')

plt.subplot(2, 2, 3)
sns.histplot(loan_df['LoanAmount'], bins=20, kde=True)
plt.title('Distribution of Loan Amount')

plt.subplot(2, 2, 4)
sns.countplot(x='Loan_Status', data=loan_df)
plt.title('Loan Status Count')
plt.show()

# Visualize correlations between numerical columns
plt.figure(figsize=(8, 6))
sns.heatmap(loan_df[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
