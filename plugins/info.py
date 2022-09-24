# USER INFORMATION COMMAND
from datetime import datetime
import time
import pymongo
from telegraph import upload_file
import pymongo.errors
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

from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest, Forbidden


@Client.on_message(filters.command('info',prefixes=['.','/','!'],case_sensitive=False))
@Client.on_message(filters.command('myacc',prefixes=['.','/','!'],case_sensitive=False))
async def info(Client, message):
        verified_gps = open('files/groups.txt', 'r').readlines()
        if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
            await message.reply_text(text= group_not_allowed,reply_to_message_id=message.message_id)
        else:
            msg = await message.reply_text(text="<b>Please Wait...</b>",reply_to_message_id=message.message_id)
            await Client.send_chat_action(message.chat.id, "typing")
            find = maindb.find_one({
                "_id": message.from_user.id,
            })
            if isinstance(find, type(None)) == True:
                text = """<b>⚠️ Use /register to Register Yourself..! ⚠️</b>"""
                await msg.edit_text(text)
            else:
                if  "Hee" == True:
                    text = """<b>⚠️ Use /register to Register Yourself..! ⚠️</b>"""
                    await msg.edit_text(text)
                else:
                    antispam_time = "Hee"
                    text = f"""
<b>〄 User Information :- </b> 

<b>●</b> First Name: <b>{message.from_user.first_name}</b>
<b>●</b> User Name: <b>{message.from_user.username}</b>
<b>●</b> User Id: <b><code>{message.from_user.id}</code></b>
<b>●</b> Limited: <b>{message.from_user.is_restricted}</b>
<b>●</b> Profile Link: <b><a href="tg://user?id={message.from_user.id}">Click Here</a></b>
<b>●</b> Profile Image: <b><a href="{find['image']}">Click Here</a></b>


<b>〄 User Database Information :- </b> 

<b>●</b> Role: <b>{find['role']}</b>
<b>●</b> Plan: <b>{find['plan']}</b>
<b>●</b> Status: <b>{find['status']}</b>
<b>●</b> Credits: <b>{find['credits']}</b>
<b>●</b> AntiSpam Time: <b>{antispam_time}</b>


<b>〄 Chat Information :- </b> 

<b>●</b> Chat Name: <b>{message.chat.title}</b>
<b>●</b> User Name: <b>{message.chat.username}</b>
<b>●</b> Chat Id: <b><code>{message.chat.id}</code></b>
<b>●</b> Chat Type: <b>{message.chat.type.capitalize()}</b>
    """
                    await msg.edit_text(text,disable_web_page_preview=True)