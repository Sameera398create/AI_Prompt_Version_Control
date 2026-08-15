import pandas as pd

# Read the real Dolly 15K dataset
df = pd.read_json("databricks-dolly-15k.jsonl", lines=True)

print("========== DATASET INFORMATION ==========")

# Total records
print("Total records:", len(df))

# Columns
print("\nColumns:")
print(df.columns.tolist())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate instructions
print("\nDuplicate instructions:")
print(df["instruction"].duplicated().sum())

# Category distribution
print("\nCategory distribution:")
print(df["category"].value_counts())

# Average instruction length
df["instruction_length"] = df["instruction"].str.len()

# Average response length
df["response_length"] = df["response"].str.len()

print("\nAverage instruction length:",
      round(df["instruction_length"].mean(), 2))

print("Average response length:",
      round(df["response_length"].mean(), 2))

# Display one complete example
print("\n========== SAMPLE RECORD ==========")

print("Instruction:")
print(df.iloc[0]["instruction"])

print("\nContext:")
print(df.iloc[0]["context"])

print("\nResponse:")
print(df.iloc[0]["response"])

print("\nCategory:")
print(df.iloc[0]["category"])