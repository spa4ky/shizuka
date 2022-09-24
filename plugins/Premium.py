import time
from pyrogram import Client
import requests
import re
import bs4
from values import *
from pyrogram import Client, filters
import json


@Client.on_message(filters.command(["premium"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)
async def sf(Client, message):
  credits = message.text.split(None, 1)[1]
  r_msg = message.reply_to_message
  iuser = r_msg.from_user.id
  if message.from_user.id == 1846020026:
    maindb.update_one({'_id': iuser},{
      '$set': {
        "plan": "PAID PLAN",
        "role": "PAID USER",
        "status": "P",
        "credits": credits
      }}, upsert=False)
    await message.reply_text("<b>Success</b>")
  else:
    return await message.reply("Heh nigga")
