import os
import pyrogram
from pyrogram.types.bots_and_keyboards import inline_keyboard_button
from values import *
from pyrogram import filters, Client
from pyrogram import client
from pyrogram.methods import messages
import pyrogram.errors
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest, Forbidden
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery, update)




async def myacc(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('💳 My Lives 💳', callback_data='mylives'),
        InlineKeyboardButton('➡️ Gates ➡️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  find = maindb.find_one({
    "_id": message.reply_to_message.from_user.id,
})
  if isinstance(find, type(None)) == True:
    text = """<b>⚠️ Use /register to Register Yourself..! ⚠️</b>"""
    await Client.answer_callback_query(
            callback_query_id=update.id,
            text=text,
            show_alert="true"
          )
  else:
    antispam_time = int(antidb.get(message.reply_to_message.from_user.id).decode("utf-8"))
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
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=reply_markup,
        message_id=message.message_id,
        disable_web_page_preview=True
    )










# GATES HELP MENU 
async def gates(Client, message,update):
  buttons = [
  [
      InlineKeyboardButton('🟢 Free 🟢', callback_data='free'), 
      InlineKeyboardButton('💰 Paid 💰', callback_data='paid')
  ],
  [
      InlineKeyboardButton('️⚙️ Tools ⚙️', callback_data='tools'),
      InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')

  ]
  ]
    
  reply_markup = InlineKeyboardMarkup(buttons)
  text="""<b>Seems like You are interested in my Commands?

Press Below buttons to know my Commands</b>"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )










# PAID COMMANDS HELP
async def paid(Client, message,update):
  buttons = [
  [
      InlineKeyboardButton('🟢 Auth 🟢', callback_data='auth'), 
      InlineKeyboardButton('🔴 Charge 🔴', callback_data='charge')
  ],
  [
      InlineKeyboardButton('🟣 Extra 🟣', callback_data='extra'),
      InlineKeyboardButton('️⚙️ Tools ⚙️', callback_data='tools')
  ],
  [
      InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
  ]
  ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text="""Seems like You are interested in my Paid Commands?

Press Below buttons to know my Paid Commands</b>"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )










# FREE GATES HELP
async def free(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('⬅️ Back ⬅️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
FREE
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )










# AUTH GATES HELP MENU
async def auth(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('️⬅️ Back ⬅️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
AUTH
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )
  










# CHARGE GATES HELP
async def charge(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('️⬅️ Back ⬅️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
CHARGE
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )










# EXTRA GATES HELP
async def extra(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('️⬅️ Back ⬅️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
EXTRA
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )











#BOT BUY MESSAGE
async def buy(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('💰 Buy 💰', url='https://t.me/SPA4KY')
    ],
    [
        InlineKeyboardButton('️⬅️ Back ⬅️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
BUY
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )










## CC GENERATOR COMMAND
async def gen(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('⬅️ Back ⬅️', callback_data='gates'),
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  msg = re.search(r'Your Data = (.*).\n', update.message.text).group(1)
  input = re.findall(r"[0-9]+", msg)
  if len(input) == 0:
      text = "Your Bin Is Empty"
      await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
  if len(input) == 1:
      cc = input[0]
      mes = 'x'
      ano = 'x'
      cvv = 'x'
  elif len(input[0]) < 6 or len(input[0]) > 16:
      text = "Your Bin Is Incorrect"
      await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
  if len(input) == 2:
      cc = input[0]
      mes = input[1]
      ano = 'x'
      cvv = 'x'
  if len(input) == 3:
      cc = input[0]
      mes = input[1]
      ano = input[2]
      cvv = 'x'
  if len(input) == 4:
      cc = input[0]
      mes = input[1]
      ano = input[2]
      cvv = input[3]
  else:
      if len(cc) > 15:
          await msg.edit_text("Your Bin Is Invalid.")
          await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
      else:
        bin = cc[:6]
        res = requests.get("https://bin-check-dr4g.herokuapp.com/api/" + bin)
        if res.status_code != requests.codes.ok or json.loads(res.text)['result'] == False:
            text = "Your Bin Is Invalid."
            await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
        elif str(bin) + "\n"in banned_bins or "PREPAID" in res.text:
            text = "Your Bin Is Banned."
            await Client.edit_message_text(chat_id=message.chat.id,text=text,reply_markup=reply_markup,message_id=message.message_id)
        else:
            bin_data = json.loads(res.text)
            cc_gen(cc,mes,ano,cvv)
            cards = ''.join(ccs)
            ccs.clear()
            text = f""""
<b>❇️ [RANDOM CC GENERATOR] ❇️

✘ BIN: {cc}|{mes}|{ano}|{cvv}
✘ BANK INFO: {bin_data['data']['bank']} - {bin_data['data']['countryInfo']['code']}({bin_data['data']['countryInfo']['emoji']})
✘ BIN INFO: <code>{bin}</code> - {bin_data['data']['level']} - {bin_data['data']['type']}
┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ 

<code>{cards} </code></b>"""       
            buttons = [[InlineKeyboardButton('🔄 Gen Again 🔄', callback_data='gen')]]   
            reply_markup = InlineKeyboardMarkup(buttons)
            await Client.edit_message_text(
                chat_id=message.chat.id,
                text=text,
                reply_markup=reply_markup,
                message_id=message.message_id,
                disable_web_page_preview=True
  )











# TOOLS MENU
async def tools(Client, message , update):
  buttons = [
    [
        InlineKeyboardButton('️⬅️ Back ⬅️', callback_data='gates')
    ],
    [
        InlineKeyboardButton('❗️ Exit ❗️', callback_data='close')
    ]
    ]
  reply_markup = InlineKeyboardMarkup(buttons)
  text = """
TOOLS
"""
  await Client.edit_message_text(
      chat_id=message.chat.id,
      text=text,
      reply_markup=reply_markup,
      message_id=message.message_id,
      disable_web_page_preview=True
  )










# BUTTON PROTECTION 
@Client.on_callback_query()
async def button(Client, update):
      cb_data = update.data
      try: 
        text = f"""✖️ Not Allowed : This Buttons is Only for {update.message.reply_to_message.from_user.first_name} [{update.message.reply_to_message.from_user.id}] ✖️"""



        if update.message.reply_to_message.from_user.id == update.from_user.id:
          if "myacc" in cb_data:
            await myacc(Client, update.message,update)
          elif "close" in cb_data:
            await update.message.delete() 
          elif "gates" in cb_data:
            await gates(Client, update.message,update)
          elif "free" in cb_data:
            await free(Client, update.message,update)
          elif "paid" in cb_data:
                await paid(Client, update.message,update)
          elif "auth" in cb_data:
                await auth(Client, update.message,update)
          elif "charge" in cb_data:
                await charge(Client, update.message,update)
          elif "extra" in cb_data:
                await extra(Client, update.message,update)
          elif "buy" in cb_data:
                await buy(Client, update.message,update)
          elif "gen" in cb_data:
                await gen(Client, update.message,update)
          elif "tools" in cb_data:
              await tools(Client, update.message,update)
          elif "mylives" in cb_data:
            await Client.answer_callback_query(
            callback_query_id=update.id,
            text="✖️ You Don't Have Any Lives Stored ✖️",
            show_alert="true"
          )
        else:
            await Client.answer_callback_query(
            callback_query_id=update.id,
            text=text,
            show_alert="true"
          )
      except RPCError as e:
          print(e)
      except BadRequest as e:
          print(e)
      except Forbidden as e:
          print(e)
