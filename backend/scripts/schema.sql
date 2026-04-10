CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE articles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    url TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    content TEXT,
    source TEXT,
    published_at TIMESTAMPTZ,
    fetched_at TIMESTAMPTZ DEFAULT now(),
    sentiment TEXT CHECK (sentiment IN ('Bullish','Bearish','Neutral')),
    impact_score INTEGER CHECK (impact_score BETWEEN 1 AND 10),
    summary TEXT,
    category TEXT,
    tickers TEXT[] DEFAULT '{}',
    embedding_id TEXT
);

CREATE TABLE entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    article_id UUID REFERENCES articles(id) ON DELETE CASCADE,
    ticker TEXT NOT NULL,
    company_name TEXT,
    mention_count INTEGER DEFAULT 1
);

CREATE TABLE alerts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    article_id UUID REFERENCES articles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    summary TEXT,
    impact_score INTEGER,
    tickers TEXT[],
    created_at TIMESTAMPTZ DEFAULT now(),
    is_read BOOLEAN DEFAULT false
);

CREATE INDEX ON articles(published_at);
CREATE INDEX ON articles(sentiment);
CREATE INDEX ON articles(category);
CREATE INDEX ON entities(ticker);
CREATE INDEX ON alerts(created_at);
CREATE INDEX ON alerts(is_read);
