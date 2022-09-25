# BUY PREMIUM COMMAND
from pymongo.errors import *
from values import *
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


@Client.on_message(filters.command(['price','buy' ,'purchase', f'buy@{BOT_USERNAME}' , f'price@{BOT_USERNAME}', f'purchase@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def register(Client,message):
    try: 
        buttons = [[InlineKeyboardButton('💰 BUY💰', callback_data='buy')]]
        reply_markup = InlineKeyboardMarkup(buttons)
        text = """<b>Glad to hear that You are interested in knowing my Paid Plans...!!</b>

<b>Click Below Buttons to Know My Plans.!❤️

✘ POWERED BY: <a href="tg://openmessage?user_id=1846020026">S P A R K Y</a></b>
"""
        await message.reply_text(text=text,reply_to_message_id=message.message_id,reply_markup=reply_markup)
    except Exception as e:
        print(e)