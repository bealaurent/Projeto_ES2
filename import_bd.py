import psycopg2
import json

# Conexão com o banco
conn = psycopg2.connect(
    host="localhost",
    database="Issues",
    user="",
    password=""
)
cur = conn.cursor()

# Ler arquivo JSON
with open("issues_dump.json", "r") as f:
    issues = json.load(f)

# Inserir dados no banco
for issue in issues:
    cur.execute(
        """
        INSERT INTO issues (issue_id, title, body, created_at, closed_at, user_author, user_assigned, labels)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            issue["id"],
            issue["title"],
            issue.get("body", ""),
            issue["created_at"],
            issue["closed_at"],
            issue["user"]["login"],
            issue.get("assignee", {}).get("login"),
            [label["name"] for label in issue.get("labels", [])]
        )
    )

conn.commit()
cur.close()
conn.close()
