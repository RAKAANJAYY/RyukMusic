from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ **Cara Memakai 𝙆𝙂𝙎𝙩𝙧𝙚𝙖𝙢𝙑𝙞𝙙𝙚𝙤!**

• ᴘᴇʀᴛᴀᴍᴀ,ᴍᴀsᴜᴋᴀɴ sᴀʏᴀ ᴋᴇɢʀᴏᴜᴘ.
• ᴊᴀᴅɪᴋᴀɴ sᴀʏᴀ ᴀᴅᴍɪɴ.
• ᴀᴅᴅ ᴜsᴇʀʙᴏᴛ ᴋᴇᴅᴀʟᴀᴍ ɢʀᴏᴜ.
• ɴʏᴀʟᴀᴋᴀɴ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ sᴇʙᴇʟᴜᴍ sᴛʀᴇᴀᴍɪɴɢ.
• ᴋᴇᴛɪᴋ /stream (ʀᴇᴘʟʏ ᴠɪᴅᴇᴏɴʏᴀ) ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ sᴛʀᴇᴀᴍɪɴɢ.
• ᴋᴇᴛɪᴋ /stop ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ sᴛʀᴇᴀᴍɪɴɢ

⚡ __𝙈𝘼𝙄𝙉𝙏𝘼𝙄𝙉𝙀𝘿 𝘽𝙔 𝙆𝙂𝙋𝙍𝙊𝙅𝙀𝘾𝙏__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ᴋᴇᴍʙᴀʟɪ", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"👋 **Hai!!Saya Adalah 𝙆𝙂𝙎𝙩𝙧𝙚𝙖𝙢𝙑𝙞𝙙𝙚𝙤**\n\n⚡ **Saya dibuat untuk melakukan streaming video dalam obrolan video grup dengan mudah..**\n\n❓ **Untuk mengetahui cara menggunakan saya, silakan tekan tombol bantuan di bawah ini** 👇🏻",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "➕ᴛᴀᴍʙᴀʜᴋᴀɴ sᴀʏᴀ ᴋᴇ ɢʀᴏᴜᴘ➕", url=f"https://t.me/KGvidstream_bot?startgroup=true")
                       ],[
                          InlineKeyboardButton(
                             "ɢʀᴏᴜᴘ", url=f"https://t.me/KGSupportgroup"),
                          InlineKeyboardButton(
                             "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/rakasupport")
                       ],[
                          InlineKeyboardButton(
                             "ɪɴғᴏ", callback_data="cbinfo"),
                          InlineKeyboardButton(
                             "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/knsgnwn")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🕵🏻‍♂️ **Informasi 𝙆𝙂𝙎𝙩𝙧𝙚𝙖𝙢𝙑𝙞𝙙𝙚𝙤**

🕵🏻‍♂️ 𝑩𝒐𝒕 𝒊𝒏𝒊 𝒅𝒊𝒃𝒖𝒂𝒕 𝒖𝒏𝒕𝒖𝒌 𝒎𝒆𝒍𝒂𝒌𝒖𝒌𝒂𝒏 𝒔𝒕𝒓𝒆𝒂𝒎𝒊𝒏𝒈 𝒗𝒊𝒅𝒆𝒐 𝒅𝒂𝒍𝒂𝒎 𝒐𝒃𝒓𝒐𝒍𝒂𝒏 𝒗𝒊𝒅𝒆𝒐 𝒈𝒓𝒖𝒑 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎!!

👇𝙎𝘼𝙉𝙂 𝙄𝙉𝙎𝙋𝙄𝙍𝘼𝙏𝙊𝙍‼️

🕵🏻‍♂️ » [KG](https://github.com/kalolonte1)
👩🏻‍✈️ » [Levina](https://github.com/levina-lab)
🤵🏻 » [Sammy-XD](https://github.com/Sammy-XD)
🤵🏻 » [Achu](https://github.com/Achu2234)

__This bot licensed under GNU-GPL 3.0 License__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ᴋᴇᴍʙᴀʟɪ", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
