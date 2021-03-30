import telegram
import time
from datetime import datetime
import crawl_rss as cr
from tokens import Token

my_token = Token.telegram_token
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
chat_id = Token.telegram_id

print("bot start!")

content = cr.messageFormat()

try:
    bot.sendMessage(chat_id=chat_id, text=content)

# try:
#     while(True):
#         count=0
#         while(True):
#             if(datetime.today().hour == 7 and datetime.today().minute == 0 and datetime.today().second == 0):
#                 count += 1
#                 if count == 1:
#                   content = cr.messageFormat()
#                   bot.sendMessage(chat_id=chat_id, text=content)
#                 elif count==100:
#                     break


except Exception as e:
    print("bot dead")
    print(e)
    bot.sendMessage(chat_id=Token.telegram_bot_id, text="bot dead")
