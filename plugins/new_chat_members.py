# WELCOME AND GOODBYE FUNCTION
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


@Client.on_message(filters.new_chat_members)
async def start(Client, message):
    await message.reply_text("Welcome Dear user..!❤️")
    
@Client.on_message(filters.left_chat_member)
async def end(Client, message):
    await message.reply_text("Good Bye..!👋")