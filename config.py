from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "13399054"))
API_HASH = getenv("API_HASH", "585801d590dac4c79aeaa7bcda495e62")

TOKEN = getenv("TOKEN", "6009759960:AAEMrabQKJcYXvw3QwNLDHryQ0IGniDYkJU")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://moni1:ammu@cluster0.lmgyalw.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6138249224))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tamil_chating_junctions")

LOGGER_ID = getenv("LOGGER_ID", "-1001932337367")
