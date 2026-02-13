import pandas as pd

# Load CSV
df = pd.read_csv("Azure_Weather_2025_Extended.csv")

print("Data Loaded Successfully")
print(df.head())

# Convert timestamp
df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%d-%m-%Y %H:%M", errors="coerce")

# Sort
df = df.sort_values(by="Timestamp")

# Find duplicates
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# Drop duplicates
df = df.drop_duplicates()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned file
df.to_csv("Azure_Weather_2025_Cleaned.csv", index=False)

print("\nCleaned File Saved!")


