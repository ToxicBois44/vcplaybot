 import os
from VCPlayBot.config import SOURCE_CODE
from VCPlayBot.config import ASSISTANT_NAME
from VCPlayBot.config import PROJECT_NAME
from VCPlayBot.config import SUPPORT_GROUP
from VCPlayBot.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**𝙷𝚎𝚕𝚕𝚘𝚊𝚠 👋 [{}](tg://user?id={})!**\n\n🤖 𝙸 𝚊𝚖 𝚊𝚗 𝚊𝚍𝚟𝚊𝚗𝚌𝚎𝚍 𝚋𝚘𝚝 𝚌𝚛𝚎𝚊𝚝𝚎𝚍 𝚏𝚘𝚛 𝚙𝚕𝚊𝚢𝚒𝚗𝚐 𝚖𝚞𝚜𝚒𝚌 𝚒𝚗 𝚝𝚑𝚎 𝚟𝚘𝚒𝚌𝚎 𝚌𝚑𝚊𝚝𝚜 𝚘𝚏 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙶𝚛𝚘𝚞𝚙𝚜 & 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜.\n\n✅ 𝚂𝚎𝚗𝚍 𝚖𝚎 /𝚑𝚎𝚕𝚙 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚒𝚗𝚏𝚘.\n\n 𝙹𝚘𝚒𝚗 @Cineflixlk"
      HELP_MSG = [
        ".",
f"""
**𝙷𝚎𝚕𝚕𝚘𝚊𝚠 👋 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝙱𝚊𝚌𝚔 𝚝𝚘 {PROJECT_NAME}

⚪️ {PROJECT_NAME} 𝚌𝚊𝚗 𝚙𝚕𝚊𝚢 𝚖𝚞𝚜𝚒𝚌 𝚒𝚗 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙'𝚜 𝚟𝚘𝚒𝚌𝚎 𝚌𝚑𝚊𝚝 𝚊𝚜 𝚠𝚎𝚕𝚕 𝚊𝚜 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚟𝚘𝚒𝚌𝚎 𝚌𝚑𝚊𝚝𝚜

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**

Join @Cineflixlk
""",

f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

Join @Girls_And_Boys_Chatting
""",
f"""
**Commands**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*𝙿𝚕𝚊𝚢𝚎𝚛 𝚌𝚖𝚍 𝚊𝚗𝚍 𝚊𝚕𝚕 𝚘𝚝𝚑𝚎𝚛 𝚌𝚖𝚍𝚜 𝚎𝚡𝚌𝚎𝚙𝚝 /𝚙𝚕𝚊𝚢, /𝚌𝚞𝚛𝚛𝚎𝚗𝚝  𝚊𝚗𝚍 /𝚙𝚕𝚊𝚢𝚕𝚒𝚜𝚝  𝚊𝚛𝚎 𝚘𝚗𝚕𝚢 𝚏𝚘𝚛 𝚊𝚍𝚖𝚒𝚗𝚜 𝚘𝚏 𝚝𝚑𝚎 𝚐𝚛𝚘𝚞𝚙.
𝙹𝚘𝚒𝚗 @Cineflixlk
""",

f"""
**=>> Channel Music Play 🛠**

⚪️ 𝙵𝚘𝚛 𝚕𝚒𝚗𝚔𝚎𝚍 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗𝚜 𝚘𝚗𝚕𝚢:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
Join @Cineflixlk
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
Join @Cineflixlk
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
Join @Cineflixlk
""",

f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups
Join @Cineflixlk
"""
      ]
