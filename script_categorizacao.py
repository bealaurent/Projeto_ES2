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

# Atualizar Banco
temas = {
    "arquitetura_software": ["performance", "scalability", "modular"],
    "padroes_estilos_arquiteturais": ["MVC", "REST", "serverless"],
    "padroes_de_projeto": ["singleton", "factory", "observer"]
}

cur = conn.cursor()
cur.execute("SELECT id, title, body FROM issues")
issues = cur.fetchall()

for issue in issues:
    issue_id, title, body = issue
    temas_relacionados = []

    for tema, palavras in temas.items():
        if any(p in (title + body).lower() for p in palavras):
            temas_relacionados.append(tema)

    cur.execute(
        """
        UPDATE issues
        SET tema_relacionado = %s
        WHERE id = %s
        """,
        (temas_relacionados, issue_id)
    )

conn.commit()
cur.close()
