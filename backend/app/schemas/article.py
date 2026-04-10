import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ArticleBase(BaseModel):
    url: str
    title: str
    content: str | None = None
    source: str | None = None
    published_at: datetime | None = None
    sentiment: str | None = None
    impact_score: int | None = None
    summary: str | None = None
    category: str | None = None
    tickers: list[str] = Field(default_factory=list)
    embedding_id: str | None = None


class ArticleCreate(ArticleBase):
    pass


class ArticleResponse(ArticleBase):
    id: uuid.UUID
    fetched_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
