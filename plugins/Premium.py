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
  credits = message.text
  if message.from_user.id == 5111959652:
    maindb.update_one({'_id': message.from_user.id},{
      '$set': {
        "plan": "PAID PLAN",
        "role": "PAID USER",
        "status": "P",
        "credits": credits
      }}, upsert=False)
    await message.reply_text("Success")
  else:
    return await message.reply("Heh nigga")
