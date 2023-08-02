
from pyrogram import Client
import asyncio
from VCPlayBot.config import SUDO_USERS
from VCPlayBot.config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from VCPlayBot.services.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "𝙷𝚎𝚕𝚕𝚘𝚊𝚠 𝚝𝚑𝚎𝚛𝚎, 𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊 𝚖𝚞𝚜𝚒𝚌 𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝚜𝚎𝚛𝚟𝚒𝚌𝚎 .\n\n ❗️ Rules:\n   - 𝙽𝚘 𝚌𝚑𝚊𝚝𝚝𝚒𝚗𝚐 𝚊𝚕𝚕𝚘𝚠𝚎𝚍\n   - 𝙽𝚘 𝚜𝚙𝚊𝚖 𝚊𝚕𝚕𝚘𝚠𝚎𝚍 \n\n 👉 **𝚂𝙴𝙽𝙳 𝙶𝚁𝙾𝚄𝙿 𝙸𝙽𝚅𝙸𝚃𝙴 𝙻𝙸𝙽𝙺 𝙾𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙸𝙵 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙰𝙽'𝚃 𝙹𝙾𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿.**\n\n ⚠️ 𝙳𝚒𝚜𝚌𝚕𝚊𝚖𝚎𝚛: 𝙸𝚏 𝚢𝚘𝚞 𝚊𝚛𝚎 𝚜𝚎𝚗𝚍𝚒𝚗𝚐 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚑𝚎𝚛𝚎 𝚒𝚝 𝚖𝚎𝚊𝚗𝚜 𝚊𝚍𝚖𝚒𝚗 𝚠𝚒𝚕𝚕 𝚜𝚎𝚎 𝚢𝚘𝚞𝚛 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚊𝚗𝚍 𝚓𝚘𝚒𝚗 𝚌𝚑𝚊𝚝\n    - 𝙳𝚘𝚗'𝚝 𝚊𝚍𝚍 𝚝𝚑𝚒𝚜 𝚞𝚜𝚎𝚛 𝚝𝚘 𝚜𝚎𝚌𝚛𝚎𝚝 𝚐𝚛𝚘𝚞𝚙𝚜.\n   - 𝙳𝚘𝚗'𝚝 𝚂𝚑𝚊𝚛𝚎 𝚙𝚛𝚒𝚟𝚊𝚝𝚎 𝚒𝚗𝚏𝚘 𝚑𝚎𝚛𝚎\n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit turned off")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("𝙰𝚙𝚙𝚛𝚘𝚘𝚟𝚎𝚍 𝚝𝚘 𝙿𝙼 𝚍𝚞𝚎 𝚝𝚘 𝚘𝚞𝚝𝚐𝚘𝚒𝚗𝚐 𝚖𝚎𝚜𝚜𝚊𝚐𝚎𝚜")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()
