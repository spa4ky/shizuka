# BOT HELP MENU
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
import time
from telegraph import upload_file
from pymongo.errors import *
from values import *
from pyrogram import (
    Client,
    filters
)
from datetime import datetime


@Client.on_message(filters.command(['cmds','gates' ,'commands', f'gates@{BOT_USERNAME}' , f'cmds@{BOT_USERNAME}', f'commands@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def cmds(Client,message):
    try:
        buttons = [
        [
            InlineKeyboardButton('🟢 Free 🟢', callback_data='free'), 
            InlineKeyboardButton('💰 Paid 💰', callback_data='paid')
        ],
        [
            InlineKeyboardButton('️⚙️ Tools ⚙️', callback_data='tools'),
            InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
        ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        text="""<b>Seems like You are interested in my Commands?

Press Below buttons to know my Commands</b>"""
        await message.reply_text(text=text,reply_to_message_id=message.message_id,reply_markup=reply_markup)
    except Exception as e:
        print(e)