"""
Copyright (C) 2022-2023 by DeCode@Github, < https://github.com/TeamDeCode >.
By © https://github.com/ITZ-ZAID
This file is part of < https://github.com/TeamDeCode/DcSpamBot > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/TeamDeCode/DcSpamBot/blob/main/LICENSE >

All rights reserved.
"""

import asyncio
import random
import asyncio
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from DcSpamBot import SUDO_USER as sudo_user
from DcSpamBot.Data.Cache import RAID, PROGROUPS, PORN, PORNS
from traceback import format_exc
from typing import Tuple


    
@Client.on_message(filters.user(sudo_user) & filters.command(["raid"], [".", "!", "/"]))
async def raid(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = message.command[2]
        if not user:
            await sex.edit("**Whome should I raid?**")
            return
    userz = await client.get_users(user)
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("`Baap Ke Group Me Spam Nahi!`")
        return 
    if int(userz.id) in PORNS:
        await sex.edit("This user part on my dev")
        return
    for _ in range(quantity):
        try: 
            raid = random.choice(RAID) 
            blaze = f"[{userz.first_name}](tg://user?id={userz.id}) {raid}"
            await client.send_message(message.chat.id, blaze)         
        except FloodWait as e:
            await asyncio.sleep(e.x)

@Client.on_message(filters.user(sudo_user) & filters.command(["pornspam"], [".", "!", "/"]))
async def prd(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("`Baap Ke Group Me Spam Nahi!`")
        return    
    for _ in range(quantity):
        try: 
            file = random.choice(PORN) 
            await client.send_video(chat_id=message.chat.id, video=file)       
        except FloodWait as e:
            await asyncio.sleep(e.x)
