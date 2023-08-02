# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import authorized_users_only
from VCPlayBot.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from VCPlayBot.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Welcome user, i'm {query.message.from_user.mention}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝙰𝚕𝚕𝚘𝚠 𝚈𝚘𝚞 𝚝𝚘 𝙿𝚕𝚊𝚢 𝙼𝚞𝚜𝚒𝚌 𝙾𝚗 𝙶𝚛𝚘𝚞𝚙𝚜 𝚃𝚑𝚛𝚘𝚞𝚐𝚑 𝚃𝚑𝚎 𝙽𝚎𝚠 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖'𝚜 𝚅𝚘𝚒𝚌𝚎 𝙲𝚑𝚊𝚝𝚜 !**

💡 **𝙵𝚒𝚗𝚍 𝚘𝚞𝚝 𝚊𝚕𝚕 𝚝𝚑𝚎 𝚋𝚘𝚝'𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊𝚗𝚍 𝚑𝚘𝚠 𝚝𝚑𝚎𝚢 𝚠𝚘𝚛𝚔 𝚋𝚢 𝚌𝚕𝚒𝚌𝚔𝚒𝚗𝚐 𝚘𝚗 𝚝𝚑𝚎 » 📚 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝙱𝚞𝚝𝚝𝚘𝚗 !**

❓ **𝙵𝚘𝚛 𝙸𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝙰𝚋𝚘𝚞𝚝 𝙰𝚕𝚕 𝙵𝚎𝚊𝚝𝚞𝚛𝚎 𝚘𝚏 𝚝𝚑𝚒𝚜 𝚋𝚘𝚝,𝚓𝚞𝚜𝚝 𝚝𝚢𝚙𝚎 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "✘ 𝙰𝚍𝚍 𝚖𝚎 𝚝𝚘 𝚢𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙 ✘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❓ 𝙷𝚘𝚠 𝚝𝚘 𝚞𝚜𝚎 𝙼𝚎", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 𝙳𝚘𝚗𝚊𝚝𝚎", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 𝙾𝚏𝚏𝚒𝚌𝚒𝚊𝚕 𝙶𝚛𝚘𝚞𝚙", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📣 𝙾𝚏𝚏𝚒𝚌𝚒𝚊𝚕 𝙲𝚑𝚊𝚗𝚗𝚎𝚕", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "☬ 𝚂𝚘𝚞𝚛𝚌𝚎 𝙲𝚘𝚍𝚎 ☬", url="https://t.me/Jonathanlk"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 𝙷𝚎𝚕𝚕𝚊𝚘𝚠  𝚝𝚑𝚎𝚛𝚎, 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚑𝚎 𝚑𝚎𝚕𝚙 𝚖𝚎𝚗𝚞 !</b>

**𝚒𝚗 𝚝𝚑𝚒𝚜 𝚖𝚎𝚗𝚞 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚘𝚙𝚎𝚗 𝚜𝚎𝚟𝚎𝚛𝚊𝚕 𝚊𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚖𝚎𝚗𝚞𝚜, 𝚒𝚗 𝚎𝚊𝚌𝚑 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚖𝚎𝚗𝚞 𝚝𝚑𝚎𝚛𝚎 𝚒𝚜 𝚊𝚕𝚜𝚘 𝚊 𝚋𝚛𝚒𝚎𝚏 𝚎𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 𝚘𝚏 𝚎𝚊𝚌𝚑 𝚌𝚘𝚖𝚖𝚊𝚗𝚍**

⚡ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HELP", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the basic commands</b>

🎧 [ GROUP VC CMD ]

- /play (song name) - play song from youtube
- /ytpplay (song name) - play song directly from youtube 
- /playlist - show the list song in queue
- /song (song name) - download song from youtube
- /search (video name) - search video from youtube detailed
- /video (video name) - download video from youtube detailed
- /lyrics - (song name) lyrics scrapper

🎧 [ CHANNEL VC CMD ]

- /cplay - stream music on channel voice chat
- /cplayer - show the song in streaming
- /cpause - pause the streaming music
- /cresume - resume the streaming was paused
- /cskip - skip streaming to the next song
- /cend - end the streaming music
- /admincache - refresh the admin cache
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/admincache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
/rmd - remove all downloaded files
/clean - Remove all raw files

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

💡 **Feature:** 𝚝𝚑𝚒𝚜 𝚏𝚎𝚊𝚝𝚞𝚛𝚎 𝚌𝚘𝚗𝚝𝚊𝚒𝚗𝚜 𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗𝚜 𝚝𝚑𝚊𝚝 𝚌𝚊𝚗 𝚋𝚊𝚗, 𝚖𝚞𝚝𝚎, 𝚞𝚗𝚋𝚊𝚗, 𝚞𝚗𝚖𝚞𝚝𝚎 𝚞𝚜𝚎𝚛𝚜 𝚒𝚗 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙.

𝚊𝚗𝚍 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚊𝚕𝚜𝚘 𝚜𝚎𝚝 𝚊 𝚝𝚒𝚖𝚎 𝚏𝚘𝚛 𝚝𝚑𝚎 𝚋𝚊𝚗 𝚊𝚗𝚍 𝚖𝚞𝚝𝚎 𝚙𝚎𝚗𝚊𝚕𝚝𝚒𝚎𝚜 𝚏𝚘𝚛 𝚖𝚎𝚖𝚋𝚎𝚛𝚜 𝚒𝚗 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙 𝚜𝚘 𝚝𝚑𝚊𝚝 𝚝𝚑𝚎𝚢 𝚌𝚊𝚗 𝚋𝚎 𝚛𝚎𝚕𝚎𝚊𝚜𝚎𝚍 𝚏𝚛𝚘𝚖 𝚝𝚑𝚎 𝚙𝚞𝚗𝚒𝚜𝚑𝚖𝚎𝚗𝚝 𝚠𝚒𝚝𝚑 𝚝𝚑𝚎 𝚜𝚙𝚎𝚌𝚒𝚏𝚒𝚎𝚍 𝚝𝚒𝚖𝚎.

❔ **usage:**

1️⃣ ban & temporarily ban user from your group:
   » type `/b username/reply to message` ban permanently
   » type `/tb username/reply to message/duration` temporarily ban user
   » type `/ub username/reply to message` to unban user

2️⃣ mute & temporarily mute user in your group:
   » type `/m username/reply to message` mute permanently
   » type `/tm username/reply to message/duration` temporarily mute user
   » type `/um username/reply to message` to unmute user

📝 note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 GO BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 GO BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 𝙷𝚎𝚕𝚕𝚊𝚘𝚠  𝚝𝚑𝚎𝚛𝚎, 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚑𝚎 𝚑𝚎𝚕𝚙 𝚖𝚎𝚗𝚞 !</b>

**𝚒𝚗 𝚝𝚑𝚒𝚜 𝚖𝚎𝚗𝚞 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚘𝚙𝚎𝚗 𝚜𝚎𝚟𝚎𝚛𝚊𝚕 𝚊𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚖𝚎𝚗𝚞𝚜, 𝚒𝚗 𝚎𝚊𝚌𝚑 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚖𝚎𝚗𝚞 𝚝𝚑𝚎𝚛𝚎 𝚒𝚜 𝚊𝚕𝚜𝚘 𝚊 𝚋𝚛𝚒𝚎𝚏 𝚎𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 𝚘𝚏 𝚎𝚊𝚌𝚑 𝚌𝚘𝚖𝚖𝚊𝚗𝚍**

⚡ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) 𝚏𝚒𝚛𝚜𝚝, 𝚊𝚍𝚍 𝚖𝚎 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙.
2.) 𝚝𝚑𝚎𝚗 𝚙𝚛𝚘𝚖𝚘𝚝𝚎 𝚖𝚎 𝚊𝚜 𝚊𝚍𝚖𝚒𝚗 𝚊𝚗𝚍 𝚐𝚒𝚟𝚎 𝚊𝚕𝚕 𝚙𝚎𝚛𝚖𝚒𝚜𝚜𝚒𝚘𝚗𝚜 𝚎𝚡𝚌𝚎𝚙𝚝 𝚊𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜 𝚊𝚍𝚖𝚒𝚗.
3.) 𝚊𝚍𝚍 @{ASSISTANT_NAME} 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙 𝚘𝚛 𝚝𝚢𝚙𝚎 /𝚞𝚜𝚎𝚛𝚋𝚘𝚝𝚓𝚘𝚒𝚗 𝚝𝚘 𝚒𝚗𝚟𝚒𝚝𝚎 𝚑𝚎𝚛
4.) 𝚝𝚞𝚛𝚗 𝚘𝚗 𝚝𝚑𝚎 𝚟𝚘𝚒𝚌𝚎 𝚌𝚑𝚊𝚝 𝚏𝚒𝚛𝚜𝚝 𝚋𝚎𝚏𝚘𝚛𝚎 𝚜𝚝𝚊𝚛𝚝 𝚝𝚘 𝚙𝚕𝚊𝚢 𝚖𝚞𝚜𝚒𝚌.

⚡ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
