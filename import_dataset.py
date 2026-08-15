import pandas as pd
import mysql.connector

# Read the real Dolly dataset
df = pd.read_json("databricks-dolly-15k.jsonl", lines=True)

print("Dataset loaded:", len(df), "records")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sameera@123",
    database="ai_prompt_version_control"
)

cursor = connection.cursor()

# Insert records into prompts table
sql = """
INSERT INTO prompts
(dataset_id, instruction, context, category, dataset_source)
VALUES (%s, %s, %s, %s, %s)
"""

count = 0

for index, row in df.iterrows():

    cursor.execute(
        sql,
        (
            index + 1,
            row["instruction"],
            row["context"],
            row["category"],
            "Dolly 15K"
        )
    )

    count += 1

    if count % 1000 == 0:
        print(count, "records inserted...")

# Save changes
connection.commit()

print("\nImport completed!")
print("Total records inserted:", count)

cursor.close()
connection.close()