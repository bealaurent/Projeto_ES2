CREATE TABLE issues (
    id SERIAL PRIMARY KEY,
    issue_id INT,
    title TEXT,
    body TEXT,
    created_at TIMESTAMP,
    closed_at TIMESTAMP,
    user_author TEXT,
    user_assigned TEXT,
    labels TEXT[],
    tema_relacionado TEXT,
    resolution_time_days TIMESTAMPTZ,
    priority TEXT,
    milestone TEXT
);
