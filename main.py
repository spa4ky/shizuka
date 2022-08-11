#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'cc-bot-new',
    api_id= 3176510, #get it from https://my.telegram.org/auth
    api_hash="df02110f33f1703026c28801e5fa0731", #get it from https://my.telegram.org/auth
    bot_token="1844824479:AAHec9EzAQEmhK0H603BQ9to9kxGzoDWvEw", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")



bot.run()

        
