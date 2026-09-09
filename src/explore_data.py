import pandas as pd

# Load the dataset
df = pd.read_csv("data/loan_data_set.csv")

# Display basic dataset information
print("\n===== DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Display column names
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

# Display first five rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Check data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Check target distribution
print("\n===== LOAN STATUS DISTRIBUTION =====")
print(df["Loan_Status"].value_counts())

# Check Gender subgroup distribution
print("\n===== GENDER DISTRIBUTION =====")
print(df["Gender"].value_counts(dropna=False))

# Check Education subgroup distribution
print("\n===== EDUCATION DISTRIBUTION =====")
print(df["Education"].value_counts(dropna=False))