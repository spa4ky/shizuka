from datetime import datetime
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

REPLY_MARKUP  = InlineKeyboardMarkup([
    [
    InlineKeyboardButton('🔒 My Account 🔒', callback_data='myacc'),
    InlineKeyboardButton('➡️ Gates ➡️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
])


@Client.on_message(filters.command(['start', f'start@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def start(Client, message):
    await Client.send_chat_action(message.chat.id, "typing")
    if message.reply_to_message is not None:
        message.text = message.reply_to_message.text
        
    caption = f"""
<b>{get_part_of_day()} <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>[<code>{message.from_user.id}</code>],
[{❤️}](https://telegra.ph/file/b5d707edb1ae9c84c7e10.jpg).!❤
I Am Shizuka, an advanced multifunctional cc checker bot with many useful tools and accounts checker.

Press below buttons to know More..!

POWERED BY: <a href="tg://openmessage?user_id=1846020026">S P A R K Y<a/></b>"""
    await Client.send_message(chat_id=message.chat.id,text=caption,reply_to_message_id=message.message_id,reply_markup=REPLY_MARKUP)
