import psycopg2
import json

conn = psycopg2.connect(
    dbname="<nome do banco que vai criar>", user="<usuário do post>", password="<senha do post>", host="localhost", port="5432"
)
cur = conn.cursor()

with open("issues_dump.json", "r") as f:
    issues = json.load(f)

for issue in issues:
    cur.execute("""
        INSERT INTO issues (issue_id, titulo, descricao, data_abertura, data_conclusao, autor, atribuido)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        issue["id"], issue["title"], issue["body"], issue["created_at"], 
        issue["closed_at"], issue["user"]["login"], 
        issue["assignee"]["login"] if issue["assignee"] else None
    ))

conn.commit()
cur.close()
conn.close()