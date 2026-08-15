import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sameera@123",
        database="ai_prompt_version_control"
    )

    if connection.is_connected():
        print("MySQL connection successful!")

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")