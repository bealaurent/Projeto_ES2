import psycopg2
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import config
import psycopg2

db_config = config.CONFIG_BD

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

cursor.execute("SELECT issue_id, body FROM issues")
rows = cursor.fetchall()

pattern = r"### (.*?)\n(.*?)(?=\n###|\Z)"


for row in rows:
    issue_id = row[0]
    texto = row[1]

    
    dados = dict(re.findall(pattern, texto, re.DOTALL))

    
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
