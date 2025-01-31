import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import config
import psycopg2

db_config = config.CONFIG_BD

# 🔹 Carregar os dados do banco
query = """
SELECT issue_id, title, related_theme, time_resolution, link_to_code, user_author, labels 
FROM issues;
"""

conn = psycopg2.connect(**db_config)

df = pd.read_sql(query, conn)

# Transformando o tempo de resolução para dias
df["time_resolution"] = pd.to_timedelta(df["time_resolution"]).dt.total_seconds() / 86400

sns.set_style("whitegrid")

# 📊 1. Mostrar a média do tempo de resolução por tema
plt.figure(figsize=(10,5))
df["related_theme"] = df["related_theme"].astype(str)  # Transformando temas para string
avg_time_per_theme = df.groupby("related_theme")["time_resolution"].mean().sort_values()
sns.barplot(x=avg_time_per_theme.index, y=avg_time_per_theme.values, palette="coolwarm", hue=avg_time_per_theme.index, legend=False)  # Ajuste para evitar o aviso de depreciação
plt.xticks(rotation=45, ha="right")  # Rotacionar os rótulos de x para evitar sobreposição
plt.xlabel("Tema Relacionado")
plt.ylabel("Média do Tempo de Resolução (dias)")
plt.title("Média do Tempo de Resolução por Tema Relacionado")
plt.tight_layout()  # Ajustar o layout para evitar sobreposição
plt.savefig("grafico_tempo_resolucao.png", bbox_inches="tight")  # Salva o gráfico como PNG
plt.close()  # Fecha o gráfico

# 📊 2. Exibir os 5 autores que mais criaram issues
plt.figure(figsize=(8,5))
top_authors = df["user_author"].value_counts().head(5)
sns.barplot(x=top_authors.index, y=top_authors.values, palette="viridis", hue=top_authors.index, legend=False)  # Corrigido para evitar o aviso de depreciação
plt.xticks(rotation=45, ha="right")  # Rotacionar os rótulos de x
plt.xlabel("Usuário")
plt.ylabel("Total de Issues Criadas")
plt.title("Top 5 Usuários com Mais Issues Criadas")
plt.tight_layout()  # Ajustar o layout
plt.savefig("grafico_top_autores.png", bbox_inches="tight")  # Salva o gráfico como PNG
plt.close()  # Fecha o gráfico

# 📊 3. Gráfico de barras para mostrar a distribuição de temas (limitar aos 10 mais frequentes)
plt.figure(figsize=(10,6))  # Tamanho do gráfico
theme_count = df["related_theme"].value_counts().head(10)  # Limita aos 10 temas mais frequentes

sns.barplot(x=theme_count.index, y=theme_count.values, palette="Set2", hue=theme_count.index, legend=False)  # Corrigido para evitar o aviso de depreciação
plt.xticks(rotation=45, ha="right")  # Rotacionar os rótulos de x
plt.xlabel("Tema Relacionado")
plt.ylabel("Número de Issues")
plt.title("Distribuição de Issues por Tema Relacionado")
plt.tight_layout()  # Ajustar o layout
plt.savefig("grafico_distribuicao_tema.png", bbox_inches="tight")  # Salva o gráfico como PNG
plt.close()  # Fecha o gráfico

# 📊 4. Relacionar as labels com o tempo de resolução (limitar aos 10 mais)
df_exploded = df.explode("labels")  # Separando as labels em linhas distintas
label_time = df_exploded.groupby("labels")["time_resolution"].mean().sort_values(ascending=False).head(10)  # Limita às 10 labels com maior tempo de resolução

plt.figure(figsize=(12,6))
sns.barplot(x=label_time.index, y=label_time.values, palette="magma", hue=label_time.index, legend=False)  # Corrigido para evitar o aviso de depreciação
plt.xticks(rotation=45, ha="right")  # Rotacionar os rótulos de x
plt.xlabel("Labels")
plt.ylabel("Média do Tempo de Resolução (dias)")
plt.title("Correlação entre Labels e Tempo de Resolução")
plt.tight_layout()  # Ajustar o layout
plt.savefig("grafico_labels_tempo_resolucao.png", bbox_inches="tight")  # Salva o gráfico como PNG
plt.close()  # Fecha o gráfico
