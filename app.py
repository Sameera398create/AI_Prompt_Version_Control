from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)


# ================= DATABASE CONNECTION =================

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST", "localhost"),
        port=int(os.environ.get("MYSQLPORT", 3306)),
        user=os.environ.get("MYSQLUSER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.environ.get(
            "MYSQLDATABASE",
            "ai_prompt_version_control"
        )
    )


# ================= HOME PAGE =================

@app.route("/")
def home():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT prompt_id, instruction, context, category
        FROM prompts
        ORDER BY prompt_id
        LIMIT 100
    """)

    prompts = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        prompts=prompts
    )


# ================= SEARCH =================

@app.route("/search")
def search():

    keyword = request.args.get("keyword", "")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT prompt_id, instruction, context, category
        FROM prompts
        WHERE instruction LIKE %s
        ORDER BY prompt_id
        LIMIT 100
    """, (f"%{keyword}%",))

    prompts = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        prompts=prompts,
        keyword=keyword
    )


# ================= PROMPT DETAILS =================

@app.route("/prompt/<int:prompt_id>")
def prompt_details(prompt_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Get prompt
    cursor.execute("""
        SELECT *
        FROM prompts
        WHERE prompt_id = %s
    """, (prompt_id,))

    prompt = cursor.fetchone()

    # Get all versions
    cursor.execute("""
        SELECT *
        FROM prompt_versions
        WHERE prompt_id = %s
        ORDER BY version_number
    """, (prompt_id,))

    versions = cursor.fetchall()

    cursor.close()
    conn.close()

    if prompt is None:
        return "Prompt not found", 404

    return render_template(
        "prompt.html",
        prompt=prompt,
        versions=versions
    )


# ================= ADD NEW VERSION =================

@app.route("/add_version/<int:prompt_id>", methods=["POST"])
def add_version(prompt_id):

    new_prompt = request.form.get("prompt_text")
    change_description = request.form.get("change_description")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Find latest version number
    cursor.execute("""
        SELECT MAX(version_number)
        FROM prompt_versions
        WHERE prompt_id = %s
    """, (prompt_id,))

    result = cursor.fetchone()

    if result[0] is None:
        new_version = 1
    else:
        new_version = result[0] + 1

    # Insert new version
    cursor.execute("""
        INSERT INTO prompt_versions
        (
            prompt_id,
            version_number,
            prompt_text,
            change_description
        )
        VALUES (%s, %s, %s, %s)
    """, (
        prompt_id,
        new_version,
        new_prompt,
        change_description
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(
        url_for(
            "prompt_details",
            prompt_id=prompt_id
        )
    )


# ================= VERSION COMPARISON =================

@app.route("/compare/<int:prompt_id>/<int:version1>/<int:version2>")
def compare_versions(prompt_id, version1, version2):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Get first version
    cursor.execute("""
        SELECT *
        FROM prompt_versions
        WHERE prompt_id = %s
        AND version_number = %s
    """, (prompt_id, version1))

    v1 = cursor.fetchone()

    # Get second version
    cursor.execute("""
        SELECT *
        FROM prompt_versions
        WHERE prompt_id = %s
        AND version_number = %s
    """, (prompt_id, version2))

    v2 = cursor.fetchone()

    # Get prompt information
    cursor.execute("""
        SELECT *
        FROM prompts
        WHERE prompt_id = %s
    """, (prompt_id,))

    prompt = cursor.fetchone()

    cursor.close()
    conn.close()

    if v1 is None or v2 is None:
        return "Version not found", 404

    return render_template(
        "compare.html",
        prompt=prompt,
        v1=v1,
        v2=v2
    )


# ================= RUN APPLICATION =================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )