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
    'cc-botnew',
    api_id= 15471429, #get it from https://my.telegram.org/auth
    api_hash= "0f88e759ffe6bdd2b18d646ab23af0d2", #get it from https://my.telegram.org/auth
    bot_token="5469257798:AAHBwdccHCSQPjIPjazuUGKPRUUg03C6VPk", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")



bot.run()

        
