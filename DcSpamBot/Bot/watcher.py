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
from typing import Tuple

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from DcSpamBot import SUDO_USER
from DcSpamBot.Data.Cache import RAID, PROGROUPS, PORN, PORNS
from traceback import format_exc
from typing import Tuple
ACTIVATE_LIST = []

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])





@Client.on_message(filters.user(SUDO_USER) & filters.command(["replyraid", "rraid"], [".", "!"]))
async def gban(app: Client, message):
    Zaid = await message.reply_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await Zaid.edit("**Whome should I replyraid?**")
            return
    get_user = await app.get_users(user)
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("`Baap Ke Group Me Spam Nahi!`")
        return
    if int(get_user.id) in PORNS:
        await Zaid.edit("Chal Chal baap Ko mat sikha")
        return
    elif int(get_user.id) in SUDO_USER:
        await Zaid.edit("Abe Lawde that guy part of my sudo users.")
        return
    elif int(get_user.id) in ACTIVATE_LIST:
        await Zaid.edit("Already raid activate in this user.")
        return
    ACTIVATE_LIST.append(get_user.id)
    await Zaid.edit(f"**Successfully Reply Raid Started {get_user.first_name}!**")

@Client.on_message(filters.user(SUDO_USER) & filters.command(["dreplyraid", "drraid"], [".", "!"]))
async def gbam(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.reply_text("**Whome should I dreplyraid?**")
            return
    get_user = await app.get_users(user)
    ACTIVATE_LIST.remove(get_user.id)
    await message.reply_text(f"**Reply Raid has Been Removed {get_user.first_name}, enjoy!**")


@Client.on_message(filters.all)
async def check_and_del(app: Client, message):
    if not message:
        return
    if int(message.chat.id) in PROGROUPS:
        return
    try:
        if not message.from_user.id in ACTIVATE_LIST:
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await message.reply_text(f"{random.choice(RAID)}")
    except:
        pass
