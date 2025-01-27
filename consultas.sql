-- Consulta o número de issues por tema
SELECT tema_relacionado, COUNT(*) AS total FROM issues GROUP BY tema_relacionado;

-- Consulta o tempo médio de resolução por tema
SELECT tema_relacionado, AVG(tempo_resolucao) AS tempo_medio FROM issues GROUP BY tema_relacionado;

-- Consulta para distribuição de prioridades
SELECT prioridade, COUNT(*) AS total FROM issues GROUP BY prioridade;

-- Calcula tempo de resolução
UPDATE issues SET tempo_resolucao = EXTRACT(DAY FROM (data_conclusao - data_abertura));

Select tema_relacionado from issues where is null
ALTER TABLE issues ADD COLUMN tema_relacionado JSONB;

SELECT issue_id, body, tema_relacionado
FROM issues
WHERE tema_relacionado != '[]';

SELECT COUNT(*)
FROM issues
WHERE tema_relacionado != '[]'
  AND tema_relacionado IS NOT NULL;
