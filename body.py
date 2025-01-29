import psycopg2
import re

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="Engenharia_da_comp_2",
    user="api_user",
    password="ap1s$", 
    port=5432
)
cursor = conn.cursor()

# Query para buscar os dados da tabela 'issues' (exemplo de dados na coluna)
cursor.execute("SELECT issue_id, body FROM issues")
rows = cursor.fetchall()

# Expressão regular para capturar os dados por tópicos
pattern = r"### (.*?)\n(.*?)(?=\n###|\Z)"

# Para cada linha da tabela
for row in rows:
    issue_id = row[0]
    texto = row[1]

    # Usando regex para extrair os dados por tópico
    dados = dict(re.findall(pattern, texto, re.DOTALL))

    # Extrair cada valor com base nos tópicos
    link_to_code = dados.get("Link to the code that reproduces this issue", "").strip()
    to_reproduce = dados.get("To Reproduce", "").strip()
    current_vs_expected = dados.get("Current vs. Expected behavior", "").strip()
    environment_info = dados.get("Provide environment information", "").strip()
    affected_areas = dados.get("Which area(s) are affected? (Select all that apply)", "").strip()
    affected_stages = dados.get("Which stage(s) are affected? (Select all that apply)", "").strip()
    additional_context = dados.get("Additional context", "").strip()

    # Atualizar as colunas na tabela 'issues'
    sql_update = """
    UPDATE issues
    SET 
        link_to_code = %s,
        to_reproduce = %s,
        current_vs_expected = %s,
        environment_info = %s,
        affected_areas = %s,
        affected_stages = %s,
        additional_context = %s
    WHERE issue_id = %s;  
    """

    # Atualizando o banco de dados com as informações extraídas
    cursor.execute(sql_update, (link_to_code, to_reproduce, current_vs_expected, environment_info, affected_areas, affected_stages, additional_context, issue_id))

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print("Dados atualizados com sucesso!")
