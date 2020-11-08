from sys import argv
from chatrobot import Config
from chatrobot import chatbot
from chatrobot import logging
from pathlib import Path
from sys import argv
import telethon.utils
from telethon import TelegramClient
from chatrobot.utils import chatbot_cmd, start_chatbot
import glob



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    chatbot.start(bot_token=Config.BOT_TOKEN)
    
path = "chatrobot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_chatbot(shortname.replace(".py", ""))

print("Your ChatBot is Ready. Thank @CyberBoyAyush ❤️")
print("Try Sending /start")

if len(argv) not in (1, 3, 4):
    chatbot.disconnect()
else:
    chatbot.run_until_disconnected()
