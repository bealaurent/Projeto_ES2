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

    # Dicionário de temas
    temas = {
    "arquitetura_software": [
        "performance", "scalability", "modular", "reliability", "maintainability", 
        "extensibility", "interoperability", "adaptability", "fault tolerance", 
        "high availability", "cloud-native", "microservices", "distributed systems", 
        "event-driven", "SOA"
    ],
    "padroes_estilos_arquiteturais": [
        "MVC", "REST", "serverless", "microfrontend", "CQRS", "monolithic", 
        "hexagonal architecture", "layered architecture", "event sourcing", 
        "pipeline", "broker", "publish-subscribe", "shared-nothing", "DDD", 
        "clean architecture"
    ],
    "padroes_de_projeto": [
        "singleton", "factory", "observer", "builder", "adapter", "decorator", 
        "proxy", "strategy", "template method", "command", "chain of responsibility", 
        "state", "mediator", "flyweight", "prototype", "bridge", "visitor", 
        "composite"
    ]
    }

    
    cur.execute("SELECT issue_id, title, body FROM issues")
    issues = cur.fetchall()

    for issue in issues:
        id, title, body = issue

        
        title = title or ""
        body = body or ""

        
        temas_relacionados = []
        for tema, palavras in temas.items():
            if any(p in (title + body).lower() for p in palavras):
                temas_relacionados.append(tema)

        
        temas_json = json.dumps(temas_relacionados)

        
        cur.execute(
            """
            UPDATE issues
            SET related_theme = %s
            WHERE issue_id = %s
            """,
            (temas_json, id)
        )

    conn.commit()
    print("Dados atualizados com sucesso.")

except psycopg2.Error as e:
    print(f"Erro ao acessar o banco de dados: {e}")

finally:
    
    if 'cur' in locals() and not cur.closed:
        cur.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Conexão com o banco de dados encerrada.")
