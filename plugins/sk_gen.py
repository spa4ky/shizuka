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
import requests, random, string, time, os


sks = []
def sk_gen_tg(amount = 'x',): 
    if amount != 'x':
        amount = int(amount)
    else:
        amount = 26
    genrated = 0
    type = "short"
    while(genrated < amount):
      genrated += 1
      if type == "long":
        skkey = random.choice(['sk_live_51H', 'sk_live_51J'])+''.join(random.choices( string.digits + string.ascii_letters, k = 96))
      elif type == "short":
        skkey = "sk_live_"+''.join(random.choices( string.digits + string.ascii_letters, k = 24))
      else:
        print("Err")
      sks.append(skkey + "\n")
      
      
@Client.on_message(filters.command(["skgen", "keygen"], prefixes=[".", "/", "!"], case_sensitive=False) & filters.text)  
def sk_gen(Client, message):
  #key = message.text.split(None, 1)[1]
  sk_gen_tg()
  crd = ''.join(sks)
  with open("sks.txt", "r+") as s:
    s.write(crd)
  sks.clear()   
  message.reply_document("sks.txt")
  os.remove("sks.txt")      
