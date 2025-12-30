CREATE TABLE sport_types (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    unit TEXT,
    world_record NUMERIC,
    olympic_record NUMERIC
);

CREATE TABLE athletes (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    country TEXT,
    birth_year INTEGER,
    wins_count INTEGER DEFAULT 0
);

CREATE TABLE results (
    id SERIAL PRIMARY KEY,
    competition_name TEXT,
    event_date DATE,
    event_place TEXT,
    place INTEGER,
    result_value NUMERIC,
    sport_type_id INTEGER REFERENCES sport_types(id),
    athlete_id INTEGER REFERENCES athletes(id)
);
