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
    'cc-chkbot',
    api_id= 3176510, #get it from https://my.telegram.org/auth
    api_hash="df02110f33f1703026c28801e5fa0731", #get it from https://my.telegram.org/auth
    bot_token="5192319960:AAFvfj9DVts2QQxN2yWgkSZ3r7dQwfYEo9k", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")



bot.run()

        
