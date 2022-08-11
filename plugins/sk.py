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

@Client.on_message(filters.command(["sk"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def sk(Client, message):
  try:
    key = message.text.split(None, 1)[1]
    find = maindb.find_one({"_id": message.from_user.id})
    req = requests.get(f"https://api.sdbots.tk/sk?key={key}").json()
    response = req['response']
    sk_key = req['sk_key']
    if response == "✅ Live Key!":
      text = f"""
      <b>✅ LIVE KEY</b>      
      
      <b>KEY:</b> <code>{sk_key}</code>
      <b>♻️</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
      <b>🧑🏻‍💻| BOT BY: @MrItzMe</b>"""
      msg = await message.reply_text(text=text,reply_to_message_id=message.message_id) 
    else:
      text = f"""
      <b>❌ DEAD KEY</b>      
      
      <b>KEY:</b> <code>{sk_key}</code>
      
      <b>♻️</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]</b>
      <b>🧑🏻‍💻| BOT BY: @MrItzMe</b>"""
      msg = await message.reply_text(text=text,reply_to_message_id=message.message_id)       
  except Exception as e:
    await Client.send_message(chat_id=loggp, text=e)      
