import pandas as pd
import numpy as np
from thefuzz import process
#################### Task 1: Handling Missing Data ####################

# Read the dataset into a DataFrame
df = pd.read_csv('CTD_lesson5.csv')

# Print the original DataFrame to inspect missing values
print("Original DataFrame:")
print(df)

# Create df1 by dropping all rows that contain missing values
df1 = df.dropna()

# Print info for original DataFrame
print("Info for original df:")
df.info()

# Print info for df1 (after dropping missing values)
print("\nInfo for df1 (after dropna):")
df1.info()

# Replace missing Name values with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')

# Replace missing Age values with the mean Age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Replace missing Salary values with the median Salary
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# Replace missing Join Date values with a fixed date
df['Join Date'] = df['Join Date'].fillna('2020-01-01')

# Drop rows that still have missing values
df2 = df.dropna()

# Reset the index after dropping rows
df2 = df2.reset_index(drop=True)

# Convert Age column to integer type
df2['Age'] = df2['Age'].astype(int)

# Print the cleaned DataFrame
print("\nFinal cleaned DataFrame (df2):")
print(df2)

#################### Task 2: Data Transformation ####################

# Load the eclipses CSV file
# sep='|' is required for this dataset
df3 = pd.read_csv('eclipses.csv', sep='|')

# Print DataFrame info to inspect column types
print("DataFrame Info:")
df3.info()

# Print the first 5 rows of the DataFrame
print("\nFirst 5 rows of df3:")
print(df3.head())

# Convert Date column again, coercing errors to NaT
df3['Date'] = pd.to_datetime(df3['Date'], errors='coerce')

# Print the first 20 rows to inspect invalid dates
print("\nFirst 20 rows after date conversion:")
print(df3.head(20))

####################### Task 3: Validating Data Ranges #######################

# Replace ages less than 18 or greater than 65 with NaN
df2.loc[(df2['Age'] < 18) | (df2['Age'] > 65), 'Age'] = np.nan

# Print the DataFrame after replacing invalid ages
print("DataFrame after replacing invalid Age values with NaN:")
print(df2)

# Calculate the median age (ignores NaN automatically)
age_median = df2['Age'].median()

# Fill NaN values with the median age
df2['Age'] = df2['Age'].fillna(age_median)

# Print the DataFrame after filling NaN values
print("\nDataFrame after filling NaN Age values with median:")
print(df2)

####################### Task 4: Removing Duplicates & Outliers #######################

# Print information about df3
print("Info for df3:")
df3.info()

# Identify duplicate rows
duplicate_series = df3.duplicated()

# Print the first 10 duplicate entries (True values only)
print("\nFirst 10 duplicate rows:")
print(duplicate_series[duplicate_series == True].head(10))

# Count how many duplicates exist
print("\nDuplicate value counts:")
print(duplicate_series.value_counts())

# Remove duplicate rows (keep first occurrence by default)
df3 = df3.drop_duplicates()

# Print info after removing duplicates
print("\nInfo for df3 after removing duplicates:")
df3.info()

# Calculate median age (ignores NaN automatically)
age_median = df2['Age'].median()

# Replace outliers with the median
df2.loc[(df2['Age'] < 0) | (df2['Age'] > 100), 'Age'] = age_median

# Print DataFrame after handling outliers
print("\nDataFrame after replacing Age outliers:")
print(df2)

####################### Task 5: Standardizing Data #######################

# Convert Name to lowercase and remove leading/trailing whitespace
df['Name'] = df['Name'].str.strip().str.lower()

# Print the updated DataFrame
print("DataFrame after standardizing Name column:")
print(df)

# Group by City to see variations and counts
print("\nCity value counts:")
print(df.groupby('City').agg({'Name': 'count'}))

# Replace city name variations with standardized names
df['City'] = df['City'].replace({
    'NYC': 'New York',
    'LA': 'Los Angeles'
})

# Print the updated DataFrame
print("\nDataFrame after standardizing City names:")
print(df)


######################## Task 6 — Encoding Categorical Variables #######################

# Create a DataFrame with a categorical Color column
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Blue']
})

print("Original DataFrame:")
print(df)

# Convert color categories into numeric labels
df['Color_Label'] = df['Color'].map({
    'Red': 1,
    'Blue': 2,
    'Green': 3
})

print("\nDataFrame after Label Encoding:")
print(df)

# Create encoded columns
df_encoded = pd.get_dummies(df['Color'], prefix='Color')

print("\nEncoded DataFrame:")
print(df_encoded)


######################### Task 7 — Consolidating Messy Files (Mini Project) #########################

# Load the four CSV files
df1 = pd.read_csv("name_and_address_0.csv")
df2 = pd.read_csv("name_and_address_1.csv")
df3 = pd.read_csv("name_and_address_2.csv")
df4 = pd.read_csv("name_and_address_3.csv")

# Combine all DataFrames into one
df_all = pd.concat([df1, df2, df3, df4], ignore_index=True)

print("Combined DataFrame shape:")
print(df_all.shape)

# Count how many times each name appears
df_names = df_all.value_counts("Name")

# Names appearing more than twice are assumed correct
good_names = list(df_names[df_names > 2].index)

# Replace misspelled names with closest valid match
df_all["Name"] = df_all["Name"].map(
    lambda x: x if x in good_names else process.extractOne(x, good_names)[0]
)

# Count address occurrences
df_addresses = df_all.value_counts("Address")

# Addresses that appear more than twice are considered valid
good_addresses = list(df_addresses[df_addresses > 2].index)

# Fix misspelled addresses
df_all["Address"] = df_all["Address"].map(
    lambda x: x if x in good_addresses else process.extractOne(x, good_addresses)[0]
)

def fix_anomaly(group):
    group_na = group.dropna()
    if group_na.empty:
        return group
    mode = group_na.mode()
    if mode.empty:
        return group
    return mode.iloc[0]

df_all["Zip"] = df_all.groupby(
    ["Name", "Address"]
)["Zip"].transform(fix_anomaly)

df_all["Phone"] = df_all.groupby(
    ["Name", "Address"]
)["Phone"].transform(fix_anomaly)

# Remove duplicate rows
df_all = df_all.drop_duplicates()

print("Shape after removing duplicates:")
print(df_all.shape)

# Print final DataFrame info
print("\nFinal DataFrame Info:")
df_all.info()

# Print remaining null values
print("\nRemaining null values:")
print(df_all.isna().sum())


################################### Task 8 — Regular Expressions for Validation ###################################

# Create a Series of log entries
log_entries = pd.Series([
    "[2023-10-26 10:00:00] INFO: User logged in",
    "[2023-10-26 10:05:30] WARNING: Invalid input",
    "[2023-10-26 10:10:15] ERROR: Database connection failed"
])

# Extract timestamp, log level, and message
extracted_logs = log_entries.str.extract(
    r"\[(.*?)\]\s(\w+):\s(.*)"
)

print("Extracted log information:")
print(extracted_logs)

# Create a Series with inconsistent placeholders
text_data = pd.Series([
    "Value is {amount}.",
    "The price is [value].",
    "Cost: (number)",
    "Quantity = <qty>"
])

# Replace all placeholder patterns with <VALUE>
standardized_text = text_data.replace(
    [r"\{.*?\}", r"\[.*?\]", r"\(.*?\)", r"\<.*?\>"],
    "<VALUE>",
    regex=True
)

print("\nStandardized placeholder text:")
print(standardized_text)

# Create a sample DataFrame
df = pd.DataFrame({
    "order_id": [1, 2],
    "created_at": ["2021-01-05", "2021-01-06"],
    "updated_at": ["2021-01-07", "2021-01-08"]
})

# Select columns that end with '_at'
time_cols = df.filter(regex="_at$")

print("\nColumns ending with '_at':")
print(time_cols)

# Create a Series of order messages
orders = pd.Series([
    "Order #123 has been shipped on 2021-01-05",
    "Order #124 has been cancelled",
    "Shipment #125 confirmed on 02/06/2021"
])

# Select orders related to shipping
shipped_orders = orders[
    orders.str.contains("ship", case=False)
]

print("\nShipped-related orders:")
print(shipped_orders)



# %% [markdown]
# Most Common Data Issues Found
    # 1- Missing values in numeric and text columns
    # 2- Inconsistent data types (strings instead of numbers or dates)
    # 3- Duplicate records across multiple files
    # 4- Inconsistent text values (case differences, extra whitespace, abbreviations)
    # 5- Invalid or out-of-range values (ages, dates, zip codes)
    # 6- Spelling errors in names and addresses
    # 7- Mixed date formats causing parsing errors

# Techniques That Worked Best
    # 1- fillna() with mean/median for numeric columns
    # 2- dropna() and drop_duplicates() for structural cleanup
    # 3- pd.to_datetime(errors="coerce", format="mixed") for date handling
    # 4- String standardization using str.strip(), str.lower(), and str.upper()
    # 5- Fuzzy matching (thefuzz) for correcting spelling inconsistencies
    # 6- Regular expressions for validation, extraction, and pattern matching
