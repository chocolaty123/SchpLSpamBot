import os

class API:
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]

class TOKENS:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    BOT_TOKEN_2 = os.environ["BOT_TOKEN_2"]
    BOT_TOKEN_3 = os.environ["BOT_TOKEN_3"]
    BOT_TOKEN_4 = os.environ["BOT_TOKEN_4"]
    BOT_TOKEN_5 = os.environ["BOT_TOKEN_5"]
    BOT_TOKEN_6 = os.environ["BOT_TOKEN_6"]
    BOT_TOKEN_7 = os.environ["BOT_TOKEN_7"]
    BOT_TOKEN_8 = os.environ["BOT_TOKEN_8"]
    BOT_TOKEN_9 = os.environ["BOT_TOKEN_9"]
    BOT_TOKEN_10 = os.environ["BOT_TOKEN_10"]

class DATABASE:
    MONGO_DB_URL = os.environ["MONGO_DB_URL"]

class DEV:
    OWNER_ID = int(os.environ["OWNER_ID"])
    
    # DONT EDIT THIS 
    SUDO_USERS = [5868832590] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.environ["https://graph.org/file/3a2136503a930532ec61e.jpg"]
    HELP_PIC = os.environ["https://graph.org/file/3a2136503a930532ec61e.jpg"]
    START_PIC = os.environ["https://graph.org/file/3a2136503a930532ec61e.jpg"]
    COMMAND_HANDLER = os.environ["!"]
