from sqlmodel import SQLModel, Field


class pycai_auth_tokens(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    token: str = Field(unique=True)
    web_next_auth: str