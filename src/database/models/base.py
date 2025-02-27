from sqlmodel import SQLModel, Field, Relationship


class pycai_auth_tokens(SQLModel, table=True):
    id: int = Field(primary_key=True)
    token: str = Field(unique=True)
    web_next_auth: str = Field(nullable=True)
    
    bots: list['bots'] = Relationship(back_populates='auth')
    
    
class bots(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    token: str
    pycai_auth_token_id: int = Field(foreign_key='pycai_auth_tokens.id')
    character_id: str = Field(unique=True)
    
    auth: 'pycai_auth_tokens' = Relationship(back_populates='bots')
    settings: list['guild_bot_settings'] = Relationship(back_populates='bot')
    
    
class guilds(SQLModel, table=True):
    id: int = Field(primary_key=True)
    guild_id: str = Field(unique=True)
    
    settings = list['guild_bot_settings'] = Relationship(back_populates='guild')
    channels = list['channels'] = Relationship(back_populates='guild')

class guild_bot_settings(SQLModel, table=True):
    id: int = Field(primary_key=True)
    active: bool = Field(default=True)
    guild_id: int = Field(foreign_key='guilds.id')
    bot_id: int = Field(foreign_key='bots.id')
    
    guild: guilds = Relationship(back_populates='settings')
    bot: bots = Relationship(back_populates='setting')
    
    
class channels(SQLModel, table=True):
    id: int = Field(primary_key=True)
    channel_id: str = Field(unique=True)
    guild_id: int = Field(foreign_key='guilds.id')
    
    guild: guilds = Relationship(back_populates='channels')