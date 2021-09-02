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
  await query.edit_message_text(f"""👋 𝗪𝗲𝗹𝗰𝗼𝗺𝗲
⚡ **[ᏦᏀ ᗰᑌᔑᏆᑕ](https://t.me/KGSuperbot)** 𝙒𝙞𝙡𝙡 𝙋𝙡𝙖𝙮 𝙏𝙝𝙚 𝙎𝙤𝙣𝙜 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩, 𝙉𝙤𝙩 𝙊𝙣𝙡𝙮 𝙏𝙝𝙖𝙩 𝙄 𝘼𝙡𝙨𝙤 𝙃𝙖𝙫𝙚 𝘼 𝙑𝙞𝙙𝙚𝙤 𝙎𝙩𝙧𝙚𝙖𝙢 𝙁𝙚𝙖𝙩𝙪𝙧𝙚!

💡 **𝗙𝗶𝗻𝗱 𝗼𝘂𝘁 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗕𝗼𝘁'𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗮𝗻𝗱 𝗵𝗼𝘄 𝘁𝗵𝗲𝘆 𝘄𝗼𝗿𝗸 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 𝘁𝗵𝗲 » 📚 ᴄᴏᴍᴍᴀɴᴅs « !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 `/help`**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴏᴜᴘ ➕",
                        url=f"https://t.me/KGSuperbot?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/KGSupportgroup"
                    ),
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/rakasupport"),
                ],
                [
                    InlineKeyboardButton("ᴄᴀʀᴀ ᴠɪᴅsᴛʀᴇᴀᴍ", callback_data="cbguide"),
                    InlineKeyboardButton("ɪɴғᴏ ᴠɪᴅsᴛʀᴇᴀᴍ", callback_data="cbinfo"
                    ),
                ],
                [
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/knsgnwn"),
                ],
            ]
        ),
    )

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
