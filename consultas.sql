-- Consulta o número de issues por tema
SELECT tema_relacionado, COUNT(*) AS total FROM issues GROUP BY tema_relacionado;

-- Consulta o tempo médio de resolução por tema
SELECT tema_relacionado, AVG(tempo_resolucao) AS tempo_medio FROM issues GROUP BY tema_relacionado;

-- Consulta para distribuição de prioridades
SELECT prioridade, COUNT(*) AS total FROM issues GROUP BY prioridade;