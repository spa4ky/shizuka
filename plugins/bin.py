# BIN CHECK COMMAND
import requests
from pyrogram import Client
import time
import requests
from pyrogram import (
    Client,
    filters)
from values import *
import json


@Client.on_message(filters.command('bin',prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def bin(Client, message):
    try:
        started_time = time.time()
        if "hehe" == "hds":
            pass
        else:
            msg = await message.reply_text(text="<b>Please Wait...</b>",reply_to_message_id=message.message_id)
            if message.reply_to_message is not None:
                message.text = message.reply_to_message.text
            find = maindb.find_one({
                "_id": message.from_user.id,
            })
            if isinstance(find, type(None)) == True:
                await msg.edit_text(use_not_registered)
            else:
                try:
                    input = lista(message.text)
                    bin = input[0]
                except Exception as e:
                    await msg.edit_text("⚠️ Empty Bin ⚠️")
                else:
                    if len(bin) < 6:
                        await msg.edit_text("Bin Is To Short")
                    elif int(bin[0]) in waste_cards:
                        await msg.edit_text("⚠️ Invalid Bin ⚠️")
                    else:
                        req = requests.get("https://bin-check-dr4g.herokuapp.com/api/" + bin)
                        if req.status_code == requests.codes.ok and 'result":true' in req.text:
                            jsontext =  json.loads(req.text)
                            text = f"""
<b>〄 Bin Information :- </b> 

<b>●</b> Bin: <code>{jsontext['data']['bin']}</code>✅
<b>●</b> Vendor: <b>{jsontext['data']['vendor']}</b>
<b>●</b> Type: <b>{jsontext['data']['type']}</b>
<b>●</b> Level: <b>{jsontext['data']['level']}</b>
<b>●</b> Bank: <b>{jsontext['data']['bank']}</b>
<b>●</b> Country: <b>{jsontext['data']['country']}({jsontext['data']['countryInfo']['emoji']})</b>
<b>●</b> Dial Code: <b>{jsontext['data']['countryInfo']['dialCode']}</b>

<b>●</b> CHECKED BY: <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>[{find['role']}]</b>
<b>●</b> POWERED BY: <b><a href="tg://openmessage?user_id=1846020026">S P A R K Y</a></b>"""
                            await msg.edit_text(text, disable_web_page_preview=True)
                        else:
                            await msg.edit_text("⚠️ Error While Getting Bin Data ⚠️")
    except IndexError as e:
        print(e)
    except Exception as e:
        print(e)