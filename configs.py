import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23475322"))
  API_HASH = os.environ.get("API_HASH", "e00e5cebf073df8baba7db34ea0ebdc9")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7254390943:AAGr45HMuJqGCDrLobX4HTi50Z_FLtcUegI")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "File_store_56bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-102197836805"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "adrinolinks.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "80118c72026ffc6debd8d4d909af5bf753a86f4a")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6170050819"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Umarxofficiall:cappuccino6005205125.@cluster0.uwzmp5o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002187391758")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002246184289"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Umar](https://t.me/+3zQFUNujkupiZmM1)
 
  Support My Hard Work Youtuber king.

"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
