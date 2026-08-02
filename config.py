import os
from dotenv import load_dotenv
import ast

load_dotenv()
DISCORD_WEBHOOK_URL_LIST = ast.literal_eval(
    os.getenv("DISCORD_WEBHOOK_URL_LIST")
)
