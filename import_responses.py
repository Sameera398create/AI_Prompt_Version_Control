import json
import mysql.connector

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sameera@123",
    database="ai_prompt_version_control"
)

cursor = connection.cursor()

# Load dataset
with open("databricks-dolly-15k.jsonl", "r", encoding="utf-8") as file:
    records = [json.loads(line) for line in file]

print("Dataset loaded:", len(records), "records")

# Get Version 1 IDs in prompt order
cursor.execute("""
    SELECT version_id, prompt_id
    FROM prompt_versions
    WHERE version_number = 1
    ORDER BY prompt_id
""")

versions = cursor.fetchall()

insert_query = """
INSERT INTO responses
(version_id, response_text, model_name)
VALUES (%s, %s, %s)
"""

count = 0

for version, record in zip(versions, records):

    version_id = version[0]
    response_text = record["response"]

    cursor.execute(
        insert_query,
        (
            version_id,
            response_text,
            "Dolly 15K Reference"
        )
    )

    count += 1

    if count % 1000 == 0:
        print(count, "responses inserted...")

connection.commit()

print()
print("Import completed!")
print("Total responses inserted:", count)

cursor.close()
connection.close()