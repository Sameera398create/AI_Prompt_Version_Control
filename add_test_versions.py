import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sameera@123",
    database="ai_prompt_version_control"
)

cursor = connection.cursor()

sql = """
INSERT INTO prompt_versions
(prompt_id, version_number, prompt_text, change_description)
VALUES (%s, %s, %s, %s)
"""

# Version 2
cursor.execute(sql, (
    1,
    2,
    "When did Virgin Australia start operating? Give the answer in one clear sentence.",
    "Added instruction for a concise answer"
))

# Version 3
cursor.execute(sql, (
    1,
    3,
    "When did Virgin Australia start operating? Give the exact date and briefly explain its original name.",
    "Added date requirement and historical context"
))

connection.commit()

print("Version 2 and Version 3 added successfully.")

cursor.close()
connection.close()