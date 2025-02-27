from sqlite_utils import Database
import os

from common.base import *


def init_db():
    db = get_db()
    db[pycai_auth_tokens.__name__].create(
        {
            pycai_auth_tokens.id: int,
            pycai_auth_tokens.token: str,
            pycai_auth_tokens.web_next_auth: str
        },
        pk=pycai_auth_tokens.id,
        not_null=[
            pycai_auth_tokens.token
            ],
        transform=True
    )
    db[pycai_auth_tokens.__name__].create_index(
        [pycai_auth_tokens.token],
        unique=True,
        if_not_exists=True)
    db[bots.__name__].create(
        {
            bots.id: int,
            bots.name: str,
            bots.token: str,
            bots.pycai_auth_token_id: int,
            bots.character_id: str
        },
        pk=bots.id,
        not_null=[
            bots.name, 
            bots.token, 
            bots.pycai_auth_token_id,
            bots.character_id
            ],
        foreign_keys=[
            (bots.pycai_auth_token_id, pycai_auth_tokens.__name__, pycai_auth_tokens.id)
        ],
        transform=True
    )
    db[guilds.__name__].create(
        {
            guilds.id: int,
            guilds.guild_id: str
        },
        pk=guilds.id,
        not_null=[guilds.guild_id],
        transform=True
    )
    # db[guild_bot_settings.__name__].create(
    #     {
    #         guild_bot_settings.id: int,
    #         guild_bot_settings.active: bool,
    #         guild_bot_settings.guild_id: int,
    #         guild_bot_settings.bot_id: int
    #     },
    #     pk=guild_bot_settings.id,
    #     not_null=[
    #         guild_bot_settings.guild_id,
    #         guild_bot_settings.bot_id
    #         ],
    #     foreign_keys=[
    #         (guild_bot_settings.guild_id, guilds.__name__, guilds.id)
    #     ],
    #     transform=True
    # )
    db[channels.__name__].create(
        {
            channels.id: int,
            channels.channel_id: str,
            channels.guild_id: int
        },
        pk=channels.id,
        not_null=[channels.channel_id],
        foreign_keys=[
            (channels.guild_id, guilds.__name__, guilds.id)
            ],
        transform=True
    )
    db[chats.__name__].create(
        {
            chats.id: int,
            chats.chat_type: str,
            chats.bot_id: int,
            chats.chat_id: str,
            chats.turn_id: str,
            chats.channel_id: int
        },
        pk=chats.id,
        not_null=[
            chats.chat_type,
            chats.bot_id,
            chats.chat_id
            ],
        foreign_keys=[
            (chats.bot_id, bots.__name__, bots.id),
            (chats.channel_id, channels.__name__, channels.id)
        ],
        transform=True
    )
    db[candidates.__name__].create(
        {
            candidates.id: int,
            candidates.candidate_id: str,
            candidates.chat_id: int,
            candidates.is_primary: bool
        },
        pk=candidates.id,
        not_null=[
            candidates.candidate_id,
            candidates.chat_id
        ],
        foreign_keys=[
            (candidates.chat_id, chats.__name__, chats.id)
        ],
        transform=True
    )
    db[nicknames.__name__].create(
        {
            nicknames.id: int,
            nicknames.member_id: str,
            nicknames.chat_id: int,
            nicknames.name: str
        },
        pk=nicknames.id,
        not_null=[
            nicknames.member_id,
            nicknames.chat_id,
            nicknames.name
        ],
        foreign_keys=[
            (nicknames.chat_id, chats.__name__, chats.id)
        ],
        transform=True
    )
    db[bot2bot_chat_setting.__name__].create(
        {
            bot2bot_chat_setting.id: int,
            bot2bot_chat_setting.bot1_id: int,
            bot2bot_chat_setting.bot2_id: int,
            bot2bot_chat_setting.bot1_chat_id: int,
            bot2bot_chat_setting.bot2_chat_id: int,
            bot2bot_chat_setting.next_to: str,
            bot2bot_chat_setting.next_content: str,
            bot2bot_chat_setting.channel_id: int
        },
        pk=bot2bot_chat_setting.id,
        not_null=[
            bot2bot_chat_setting.bot1_id,
            bot2bot_chat_setting.bot2_id,
            bot2bot_chat_setting.bot1_chat_id,
            bot2bot_chat_setting.bot2_chat_id,
            bot2bot_chat_setting.channel_id
        ],
        foreign_keys=[
            (bot2bot_chat_setting.bot1_id, bots.__name__, bots.id),
            (bot2bot_chat_setting.bot2_id, bots.__name__, bots.id),
            (bot2bot_chat_setting.bot1_chat_id, chats.__name__, chats.id),
            (bot2bot_chat_setting.bot2_chat_id, chats.__name__, chats.id),
            (bot2bot_chat_setting.channel_id, channels.__name__, channels.id)
        ],
        transform=True
    )

def get_db():
    db = Database(os.getenv('DATABASE_FILEPATH'))
    return db