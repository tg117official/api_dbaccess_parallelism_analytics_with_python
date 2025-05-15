import pandas as pd
import numpy as np

# --------------------------------------------------
# Exercise 1: Creating a DataFrame
# --------------------------------------------------
# Task: Create a DataFrame using a dictionary
# Relevance: Understand how tabular data is created in Pandas

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
print("Exercise 1: Create a DataFrame")
print(df, "\n")

# --------------------------------------------------
# Exercise 2: Filtering Rows
# --------------------------------------------------
# Task: Filter people older than 30
# Relevance: Learn how to apply boolean conditions to rows

filtered_df = df[df["Age"] > 30]
print("Exercise 2: Filter rows where Age > 30")
print(filtered_df, "\n")

# --------------------------------------------------
# Exercise 3: Adding a New Column
# --------------------------------------------------
# Task: Add 'Salary' column
# Relevance: Learn how to expand DataFrames

df["Salary"] = [50000, 60000, 70000, 80000]
print("Exercise 3: Add a new column 'Salary'")
print(df, "\n")

# --------------------------------------------------
# Exercise 4: Sorting Data
# --------------------------------------------------
# Task: Sort by age in descending order
# Relevance: Learn to organize rows by column values

sorted_df = df.sort_values(by="Age", ascending=False)
print("Exercise 4: Sort DataFrame by Age (descending)")
print(sorted_df, "\n")

# --------------------------------------------------
# Exercise 5: Handling Missing Data
# --------------------------------------------------
# Task: Replace Bob's city with NaN and then fill it
# Relevance: Handle incomplete or missing data

df.loc[df["Name"] == "Bob", "City"] = np.nan  # Replace city with NaN
df["City"].fillna("Unknown", inplace=True)   # Fill NaN with "Unknown"
print("Exercise 5: Handle missing data (City for Bob set to Unknown)")
print(df, "\n")

# --------------------------------------------------
# Exercise 6: Grouping and Aggregation
# --------------------------------------------------
# Task: Group by City and get average Age
# Relevance: Perform group-level aggregations

grouped_df = df.groupby("City")["Age"].mean()
print("Exercise 6: Group by City and calculate average Age")
print(grouped_df, "\n")

# --------------------------------------------------
# Exercise 7: Merging DataFrames
# --------------------------------------------------
# Task: Merge with department data on Name
# Relevance: Combine datasets from different sources

department_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "IT", "Finance", "Marketing"]
})
merged_df = pd.merge(df, department_data, on="Name")
print("Exercise 7: Merge DataFrames on Name")
print(merged_df, "\n")

# --------------------------------------------------
# Exercise 8: Dropping Columns
# --------------------------------------------------
# Task: Drop the Salary column
# Relevance: Learn how to remove unnecessary columns

dropped_df = merged_df.drop(columns=["Salary"])
print("Exercise 8: Drop the 'Salary' column")
print(dropped_df, "\n")

# --------------------------------------------------
# Exercise 9: Reading and Writing Files
# --------------------------------------------------
# Task: Save to CSV and read back
# Relevance: Store and load persistent data

df.to_csv("output.csv", index=False)  # Save
read_df = pd.read_csv("output.csv")   # Read
print("Exercise 9: Write and read DataFrame to/from CSV")
print(read_df, "\n")

# --------------------------------------------------
# Exercise 10: Applying Functions
# --------------------------------------------------
# Task: Add 'Age Group' column using custom function
# Relevance: Learn to use apply with user-defined functions

def age_group(age):
    if age < 30:
        return "Young"
    elif age < 40:
        return "Mid"
    else:
        return "Senior"

df["Age Group"] = df["Age"].apply(age_group)
print("Exercise 10: Apply function to create Age Group column")
print(df, "\n")

# --------------------------------------------------
# Exercise 11: Renaming Columns
# --------------------------------------------------
# Task: Rename 'Age Group' to 'Category'
# Relevance: Clean up or customize column names

df.rename(columns={"Age Group": "Category"}, inplace=True)
print("Exercise 11: Rename 'Age Group' to 'Category'")
print(df, "\n")

# --------------------------------------------------
# Exercise 12: Resetting and Setting Index
# --------------------------------------------------
# Task: Reset index and then set 'Name' as index
# Relevance: Index manipulation and labeling

reset_df = df.reset_index(drop=True)      # Reset index
indexed_df = reset_df.set_index("Name")   # Set 'Name' as index
print("Exercise 12: Set 'Name' column as index")
print(indexed_df, "\n")

# --------------------------------------------------
# Exercise 13: Value Counts
# --------------------------------------------------
# Task: Count how many people fall in each Category
# Relevance: Quick insights from categorical data

counts = df["Category"].value_counts()
print("Exercise 13: Count of each Age Category")
print(counts, "\n")
