import time
from pyrogram import Client
import requests
from requests.exceptions import ProxyError
import re
import bs4
#from defs import *
from values import *
from pyrogram import Client, filters
import json

@Client.on_message(filters.command(["sk", "key"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def sk(Client, message):
  try:
    if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
      await message.reply_text(text="""<b>This Group Is Not Verified. Talk With <code>@MrItzMe</code> And Ask For Verification.</b>""",reply_to_message_id=message.message_id)
    else:    
      key = message.text.split(None, 1)[1]
      find = maindb.find_one({"_id": message.from_user.id})
      text = f"""
<b>Checking Your SK Please Wait...</b>

<b>KEY:</b> <code>{key}</code>

<b>♻️</b> CHECKING BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>🧑🏻‍💻| BOT BY: @MrItzMe</b>
"""      
      msg = await message.reply_text(text=text, reply_to_message_id=message.message_id)
      req = requests.get(f"https://api.sdbots.tk/sk?key={key}").json()
      response = req['response']
      sk_key = req['sk_key']
      status = req['status']
      if status == "Dead ✕":
        text = f"""
<b>❌ DEAD KEY</b>      
      
<b>KEY:</b> <code>{sk_key}</code>
<b>RESPONSE:</b> <code>{response}</code>

<b>♻️</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>🧑🏻‍💻| BOT BY: @MrItzMe</b>"""     
        msg = await msg.edit(text) 
      else:
        text = f"""
<b>✅ LIVE KEY</b>      
      
<b>KEY:</b> <code>{sk_key}</code>
<b>RESPONSE:</b> <code>{response}</code>

<b>♻️</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
<b>🧑🏻‍💻| BOT BY: @MrItzMe</b>"""
        msg = await msg.edit(text) 
  except Exception as e:
    await Client.send_message(chat_id=loggp, text=e)      
