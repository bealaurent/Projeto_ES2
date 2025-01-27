import psycopg2
import json

try:
    
    conn = psycopg2.connect(
        host="localhost",
        database="Engenharia_da_comp_2",
        user="api_user",
        password="colocar_senha",  
        port=5432                  
    )
    cur = conn.cursor()
    print("Conexão bem-sucedida com o banco de dados.")

    
    with open("issues_dump.json", "r") as f:
        issues = json.load(f)

    
    for issue in issues:
        try:
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
                    issue.get("closed_at"),  
                    issue["user"]["login"],
                    issue.get("assignee", {}).get("login") if isinstance(issue.get("assignee"), dict) else None,
                    json.dumps([label["name"] for label in issue.get("labels", [])])  # Converter lista para JSON
                )
            )
        except KeyError as e:
            print(f"Erro ao processar issue {issue.get('id')}: Campo ausente {e}")
        except psycopg2.Error as e:
            print(f"Erro ao inserir issue {issue.get('id')} no banco: {e}")

    conn.commit()
    print("Dados inseridos com sucesso no banco de dados.")

except psycopg2.Error as e:
    print(f"Erro de conexão com o banco de dados: {e}")

finally:
    
    if 'cur' in locals() and not cur.closed:
        cur.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Conexão com o banco de dados encerrada.")
