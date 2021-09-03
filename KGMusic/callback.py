from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""⚡𝙆𝙂𝙑𝙄𝘿𝙀𝙊𝙎𝙏𝙍𝙀𝘼𝙈⚡
📚 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𝙁𝙊𝙍
 • ᴛᴀᴍʙᴀʜᴋᴀɴ ʙᴏᴛ  ᴋᴇɢʀᴏᴜᴘ
 • ᴊᴀᴅɪᴋᴀɴ 𝙆𝙂𝙑𝙄𝘿𝙀𝙊𝙎𝙏𝙍𝙀𝘼𝙈 ᴀᴅᴍɪɴ,ᴄᴇᴋʟɪs sᴇᴍᴜᴀɴʏᴀ ᴋᴇᴄᴜᴀʟɪ ᴀᴅᴍɪɴ ᴀɴᴏɴɪᴍ!
 • ᴋᴇᴛɪᴋ /stream (reply video) ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴀʟɪʀᴀɴ ᴠɪᴅᴇᴏ!
 • sᴇʙᴇʟᴜᴍ ᴍᴇᴍᴜʟᴀɪ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴍᴀsᴜᴋᴀɴ @KGStreamAssistant
 • ᴋᴇᴛɪᴋ /stop ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀʜᴇɴᴛɪᴋᴀɴ ᴀʟɪʀᴀɴ ᴠɪᴅᴇᴏ!
 
 ⚡𝙈𝘼𝙄𝙉𝙏𝘼𝙄𝙉𝙀𝘿 𝘽𝙔 𝙆𝙂𝙋𝙍𝙊𝙅𝙀𝘾𝙏""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ᴋᴇᴍʙᴀʟɪ", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello, I am a telegram video streaming bot.**\n\n💭 **I was created to stream videos in group video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "⚙️ ɪɴғᴏ", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/knsgnwn")
                       ],[
                          InlineKeyboardButton(
                             "📍ɢʀᴏᴜᴘ", url="https://t.me/KGSupportgroup"),
                          InlineKeyboardButton(
                             "💌 ᴄʜᴀɴɴᴇʟ", url="https://t.me/rakasupport")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""⛔ 𝙄𝙉𝙁𝙊𝙍𝙈𝘼𝙎𝙄 ⛔
    
⚡ **Bot ini dibuat untuk melakukan streaming video dalam obrolan video grup telegram menggunakan beberapa metode dari WebRTC.**

📍: [KGsupport](https://t.me/KGSupportgroup]
💌: [KGchannel](https://t.me/rakasupport)
🕵🏻‍♂️: [KG](https://t.me/knsgnwn)""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ᴋᴇᴍʙᴀʟɪ", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
