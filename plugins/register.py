# REGISTER COMMAND
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
import time
from telegraph import upload_file
from pymongo.errors import *
from values import *
from pyrogram import (
    Client,
    filters
)

from datetime import datetime


@Client.on_message(filters.command(['takeme','register' ,'register ', f'register@{BOT_USERNAME}' , f'takeme@{BOT_USERNAME}', f'purchase@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def register(Client,message):
    try: 
        msg = await message.reply_text(text="<b>Please Wait...</b>",reply_to_message_id=message.message_id)
        find = maindb.find_one({
            "_id": message.from_user.id,
        })
        if find is None:
            if message.from_user.photo is None:
                userimage = "https://te.legra.ph/file/4f68128eb38ac812952e2.jpg"
            else:
                user_image_path = (f"./userimage/{message.from_user.id}.jpg")
                await Client.download_media(message=message.from_user.photo.big_file_id, file_name=user_image_path)
                tlink = upload_file(user_image_path)
                userimage = f"https://telegra.ph{tlink[0]}"
                os.remove(user_image_path)
            mydict = {
            "_id": message.from_user.id,
            "id": message.from_user.id,
            "username": message.from_user.username,
            "plan": "Free Plan",
            "role": "Free User",
            "status": "F",
            "credits": 0,
            "image": userimage
            }
            maindb.insert_one(mydict)
            antidb.set(message.from_user.id, int(time.time()))
            file = open('users.txt', 'a+') 
            file.write(str(message.from_user.id) + "\n")
            file.close()
            text = """<b>Registration Successful as a Free User..!✅️</b>"""
            await msg.edit_text(text,disable_web_page_preview=True)
        else:
            text = """<b>Registration Successful as a Free User..!✅️</b>"""
            await msg.edit_text(text,disable_web_page_preview=True)
    except Exception as e:
        print(e)