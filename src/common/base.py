class bots:
    id = 'id'
    name = 'name'
    token = 'token'
    pycai_auth_token_id = 'pycai_auth_token_id'
    character_id = 'character_id'

class pycai_auth_tokens:
    id = 'id'
    token = 'token'
    web_next_auth = 'web_next_auth'

class channels:
    id = 'id'
    channel_id = 'channel_id'
    guild_id = 'guild_id'
    
class guilds:
    id = 'id'
    guild_id = 'guild_id'

class guild_bot_settings:
    id = 'id'
    active = 'active'
    guild_id = 'guild_id'
    bot_id = 'bot_id'
    
class chats:
    id = 'id'
    chat_type = 'chat_type'
    bot_id = 'bot_id'
    chat_id = 'chat_id'
    turn_id = 'turn_id'
    channel_id = 'channel_id'

class candidates:
    id = 'id'
    candidate_id = 'candidate_id'
    chat_id = 'chat_id'
    is_primary = 'is_primary'
    
class nicknames:
    id = 'id'
    member_id = 'member_id'
    chat_id = 'chat_id'
    name = 'name'

class bot2bot_chat_setting():
    id = 'id'
    bot1_id = 'bot1_id'
    bot2_id = 'bot2_id'
    bot1_chat_id = 'bot1_chat_id'
    bot2_chat_id = 'bot2_chat_id'
    next_to = 'next_to'
    next_content = 'next_content'
    channel_id = 'channel_id'
