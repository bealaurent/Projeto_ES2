-- Consulta o número de issues por tema
SELECT related_theme, COUNT(*) AS total FROM issues GROUP BY related_theme;

-- Consulta o tempo médio de resolução por tema
SELECT related_theme, AVG(tempo_resolucao) AS tempo_medio FROM issues GROUP BY related_theme;

-- Consulta para distribuição de prioridades
SELECT prioridade, COUNT(*) AS total FROM issues GROUP BY prioridade;

-- Calcula tempo de resolução
UPDATE issues SET tempo_resolucao = EXTRACT(DAY FROM (data_conclusao - data_abertura));

Select related_theme from issues where is null
ALTER TABLE issues ADD COLUMN related_theme JSONB;

SELECT issue_id, body, related_theme
FROM issues
WHERE related_theme != '[]';

SELECT COUNT(*)
FROM issues
WHERE related_theme != '[]'
  AND related_theme IS NOT NULL;

  ##testando
