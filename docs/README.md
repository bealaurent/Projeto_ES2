# 📊 Análise de Issues do Next.js

Este projeto tem como objetivo extrair, processar e analisar issues do projeto Next.js Open Source, armazenando essas informações em um banco de dados PostgreSQL e como se relaciona com conceitos de Engenharia da computação.

## 📁 Estrutura do Projeto

```
projeto/
│── src/
│   │── body.py              # Processa e extrai informações dos issues
│   │── dados.py             # Analisa e gera gráficos sobre os issues
│   │── import_bd.py         # Importa issues do JSON para o banco de dados
│   │── script-categorizacao.py  # Categoriza os issues por tema
│   │── script_issues.py     # Coleta issues da API do GitHub
│── assets/
│── docs/
│── config.py                # Configuração do banco de dados
│── requirements.txt         # Dependências do projeto
```

## 🛠️ Pré-requisitos

Antes de começar, você precisará ter instalado:
- Python 3.8 ou superior
- PostgreSQL
- Bibliotecas listadas no `requirements.txt`

## 🚀 Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure o banco de dados no arquivo `config.py`:
   ```python
   CONFIG_BD = {
       "dbname": "seu_banco",
       "user": "seu_usuario",
       "password": "sua_senha",
       "host": "localhost",
       "port": "5432"
   }
   ```

## 📌 Como Executar

### 1️⃣ Coletar issues da API do GitHub
```sh
python src/script_issues.py
```
Baixa issues do repositório do GitHub e salva no arquivo `issues_dump.json`.

### 2️⃣ Importar os issues para o banco de dados
```sh
python src/import_bd.py
```
Lê o arquivo `issues_dump.json` e insere os dados na tabela `issues` do banco PostgreSQL.

### 3️⃣ Processar e extrair informações dos issues
```sh
python src/body.py
```
Analisa e extrai dados estruturados dos issues armazenados, atualizando a tabela `issues`.

### 4️⃣ Categorizar os issues por tema
```sh
python src/script-categorizacao.py
```
Analisa o título e a descrição dos issues e os classifica de acordo com temas pré-definidos.

### 5️⃣ Gerar análises e relatórios gráficos
```sh
python src/dados.py
```
Gera gráficos com insights sobre os issues, como tempo médio de resolução por tema.

## 📊 Exemplo de Relatório Gerado

O script `dados.py` gera gráficos que ajudam a visualizar informações, incluindo:
- Tempo médio de resolução de issues por tema (`grafico_tempo_resolucao.png`)
- Usuários que mais criaram issues (`grafico_top_autores.png`)
- Distribuição dos temas (`grafico_distribuicao_tema.png`)
- Correlação entre labels e tempo de resolução (`grafico_labels_tempo_resolucao.png`)

## 📝 Licença

Este projeto está sob a licença MIT.

---

💡 Caso tenha dúvidas ou sugestões, sinta-se à vontade para contribuir ou abrir uma issue!

