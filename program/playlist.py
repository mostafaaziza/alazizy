# Copyright (C) 2021 By Amort Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

from config import BOT_USERNAME
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from pyrogram import Client, filters
from driver.queues import QUEUE, get_queue
from driver.filters import command, other_filters


keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 إغلاق", callback_data="cls")]]
)


@Client.on_message(command(["playlist", f"playlist@{BOT_USERNAME}", "queue", f"queue@{BOT_USERNAME}"]) & other_filters)
async def playlist(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      chat_queue = get_queue(chat_id)
      if len(chat_queue)==1:
         await m.reply(f"💡 **يشتغل حاليآ:**\n\n• [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`", reply_markup=keyboard, disable_web_page_preview=True)
      else:
         QUE = f"💡 **يشتغل حاليآ:**\n\n• [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}` \n\n**📖 قائمة الانتظار:**\n"
         l = len(chat_queue)
         for x in range (1, l):
            han = chat_queue[x][0]
            hok = chat_queue[x][2]
            hap = chat_queue[x][3]
            QUE = QUE + "\n" + f"**#{x}** - [{han}]({hok}) | `{hap}`"
         await m.reply(QUE, reply_markup=keyboard, disable_web_page_preview=True)
   else:
      await m.reply("❌ **لا شي يشتغل حاليآ**")
