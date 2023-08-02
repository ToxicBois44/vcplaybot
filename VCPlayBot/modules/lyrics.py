
import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as pbot




# Lel, Didn't Get Time To Make New One So Used Plugin Made br @mrconfused and @sandy1709 dont edit credits


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("𝚂𝚎𝚊𝚛𝚌𝚑𝚒𝚗𝚐 𝙵𝚘𝚛 𝙻𝚢𝚛𝚒𝚌𝚜.....")
    query = message.text
    if not query:
        await lel.edit("`𝚆𝚑𝚊𝚝 𝙸 𝚊𝚖 𝚂𝚞𝚙𝚙𝚘𝚜𝚎𝚍 𝚝𝚘 𝚏𝚒𝚗𝚍 `")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "𝙲𝚘𝚞𝚕𝚍𝚗'𝚝 𝚏𝚒𝚗𝚍 𝚊𝚗𝚢 𝚕𝚢𝚛𝚒𝚌𝚜 𝚏𝚘𝚛 𝚝𝚑𝚊𝚝 𝚜𝚘𝚗𝚐! 𝚝𝚛𝚢 𝚠𝚒𝚝𝚑 𝚊𝚛𝚝𝚒𝚜𝚝 𝚗𝚊𝚖𝚎 𝚊𝚕𝚘𝚗𝚐 𝚠𝚒𝚝𝚑 𝚜𝚘𝚗𝚐 𝚒𝚏 𝚜𝚝𝚒𝚕𝚕 𝚍𝚘𝚎𝚜𝚗𝚝 𝚠𝚘𝚛𝚔 𝚝𝚛𝚢 `.glyrics`"
    else:
        reply = "𝚕𝚢𝚛𝚒𝚌𝚜 𝚗𝚘𝚝 𝚏𝚘𝚞𝚗𝚍! 𝚝𝚛𝚢 𝚠𝚒𝚝𝚑 𝚊𝚛𝚝𝚒𝚜𝚝 𝚗𝚊𝚖𝚎 𝚊𝚕𝚘𝚗𝚐 𝚠𝚒𝚝𝚑 𝚜𝚘𝚗𝚐 𝚒𝚏 𝚜𝚝𝚒𝚕𝚕 𝚍𝚘𝚎𝚜𝚗𝚝 𝚠𝚘𝚛𝚔 𝚝𝚛𝚢 `.glyrics`"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
