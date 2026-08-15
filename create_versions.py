import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sameera@123",
    database="ai_prompt_version_control"
)

cursor = connection.cursor()

# Get all prompts
cursor.execute("""
    SELECT prompt_id, instruction
    FROM prompts
""")

prompts = cursor.fetchall()

sql = """
INSERT INTO prompt_versions
(prompt_id, version_number, prompt_text, change_description)
VALUES (%s, %s, %s, %s)
"""

count = 0

for prompt_id, instruction in prompts:
    cursor.execute(
        sql,
        (
            prompt_id,
            1,
            instruction,
            "Original prompt from Dolly 15K"
        )
    )

    count += 1

connection.commit()

print("Version 1 created for", count, "prompts.")

cursor.close()
connection.close()