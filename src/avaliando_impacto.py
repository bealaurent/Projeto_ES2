import psycopg2
import csv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import config
import psycopg2

db_config = config.CONFIG_BD

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

# Executa uma consulta SQL
cursor.execute("SELECT title, link_to_code, related_theme, current_vs_expected, additional_context FROM issues WHERE related_theme != '[]' ")

# Obtém os resultados
rows = cursor.fetchall()

# Cabeçalhos das colunas
col_names = [desc[0] for desc in cursor.description]

# Fecha o cursor e a conexão
cursor.close()
conn.close()

# Caminho e nome do arquivo CSV
csv_file = "dados.csv"

# Escreve os dados no arquivo CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(col_names)  # Escreve os cabeçalhos
    writer.writerows(rows)  # Escreve as linhas de dados

print(f"Dados salvos em {csv_file}")
