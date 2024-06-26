import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "29023986")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "895fde5d06418650fdcce2fddebe8276") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6588152584:AAGFebSfVikwCHWs0S7nx-eB2GLadD7tBQk") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002020056630') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Venom:LostVenom@venom.bopprqu.mongodb.net/?retryWrites=true&w=majority&appName=Venom")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6756781098")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001956404845')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/28a6eaa080f619c8d55cf.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
File Name: {0}

Original File Size: {1}
Encoded File Size: {2}
Compression Percentage: {3}

Downloaded in {4}
Encoded in {5}
Uploaded in {6}
"""
