from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import ASSISTANT_NAME as an
from config import BOT_IMAGE, BOT_NAME, BOT_USERNAME, OWNER, SUPPORT_GROUP
from KGMusic.msg import Messages as tr
from helpers.filters import command


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""<b>**👋 HELLO** {message.from_user.mention}
⚡ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝗮𝗹𝗹𝗼𝘄 𝘆𝗼𝘂 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝗴𝗿𝗼𝘂𝗽𝘀 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗻𝗲𝘄 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺'𝘀 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁𝘀 !**

💡 **𝗙𝗶𝗻𝗱 𝗼𝘂𝘁 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗕𝗼𝘁'𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗮𝗻𝗱 𝗵𝗼𝘄 𝘁𝗵𝗲𝘆 𝘄𝗼𝗿𝗸 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 𝘁𝗵𝗲 » 📚 ᴄᴏᴍᴍᴀɴᴅs « !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 `/help`**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴏᴜᴘ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/rakasupport"),
                ],
                [
                    InlineKeyboardButton(text="📚 ᴄᴏᴍᴍᴀɴᴅs", url=f"https://telegra.ph/KG-Music-08-23"),
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/knsgnwn"
                    ),
                ],
            ]
        ),
    )


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""<b>ᴘᴇɴɢᴀᴛᴜʀᴀɴ
1) ᴊᴀᴅɪᴋᴀɴ ʙᴏᴛ sᴇʙᴀɢᴀɪ ᴀᴅᴍɪɴ
2) ᴍᴜʟᴀɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ
3) ᴋɪʀɪᴍ ᴘᴇʀɪɴᴛᴀʜ » /userbotjoin
➢ ᴊɪᴋᴀ ᴀssɪsᴛᴀɴᴛ ᴛᴇʟᴀʜ ʙᴇʀɢᴀʙᴜɴɢ sᴇʟᴀᴍᴀᴛ ᴍᴇɴɪᴋᴍᴀᴛɪ, 
➢ ᴊɪᴋᴀ ᴀssɪsᴛᴀɴᴛ ᴛɪᴅᴀᴋ ʙɪsᴀ ʙᴇʀɢᴀʙᴜɴɢ,sɪʟᴀᴋᴀɴ ᴍᴀsᴜᴋᴀɴ @{an} ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ sᴇᴄᴀʀᴀ ᴍᴀɴᴜᴀʟ

ᴘᴇʀɪɴᴛᴀʜ sᴇᴍᴜᴀ ᴀɴɢɢᴏᴛᴀ
➢ /play (judul lagu) - ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ʏᴀɴɢ ᴀɴᴅᴀ ᴍɪɴᴛᴀ
➢ /aplay (balas ke audio) - ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ᴅᴀʀɪ ᴀᴜᴅɪᴏ ғɪʟᴇ
➢ /ytplay (judul lagu) - ᴜɴᴛᴜᴋ ᴍᴇᴍᴜᴛᴀʀ ʟᴀɢᴜ ʏᴀɴɢ ᴀɴᴅᴀ ᴍɪɴᴛᴀ ᴛᴀɴᴘᴀ ᴘɪʟɪʜᴀɴ
➢ /song (judul lagu) - ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ʟᴀɢᴜ ᴅᴀʀɪ ʏᴏᴜᴛᴜʙᴇ
➢ /vsong (judul video) - ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ᴅᴀʀɪ ʏᴏᴜᴛᴜʙᴇ
➢ /lyrics (judul lagu) ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ʟɪʀɪᴋ ʟᴀɢᴜ
➢ /search (judul lagu/video) - ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ʟɪɴᴋ ᴅɪ ʏᴏᴜᴛᴜʙᴇ ᴅᴇɴɢᴀɴ ᴅᴇᴛᴀɪʟ

ᴘᴇʀɪɴᴛᴀʜ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ɢʀᴜᴘ
➢ /pause - ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴇᴅᴀ ᴘᴇᴍᴜᴛᴀʀᴀɴ ʟᴀɢᴜ
➢ /resume - ᴜɴᴛᴜᴋ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘᴇᴍᴜᴛᴀʀᴀɴ ʟᴀɢᴜ
➢ /skip - ᴜɴᴛᴜᴋ ᴍᴇʟᴏᴍᴘᴀᴛɪ ᴋᴇ ʟᴀɢᴜ sᴇʟᴀɴᴊᴜᴛɴʏᴀ
➢ /end - ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀʜᴇɴᴛɪᴋᴀɴ ᴘᴇᴍᴜᴛᴀʀᴀɴ ʟᴀɢᴜ
➢ /reload - ᴜɴᴛᴜᴋ sᴇɢᴀʀᴋᴀɴ ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/KGSupportgroup"
                    ),
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/knsgnwn"),
                ]
            ]
        ),
    )


help_callback_filter = filters.create(
    lambda _, __, query: query.data.startswith("helps+")
)


@Client.on_callback_query(help_callback_filter)
def helps_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split("+")[1])
    client.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=tr.HELPS_MSG[msg],
        reply_markup=InlineKeyboardMarkup(map(msg)),
    )


def map(pos):
    if pos == 1:
        button = [[InlineKeyboardButton(text="➡️", callback_data="helps+2")]]
    elif pos == len(tr.HELPS_MSG) - 1:
        url = f"https://t.me/KGSupportgroup"
        button = [[InlineKeyboardButton(text="⬅️", callback_data=f"helps+{pos-1}")]]
    else:
        button = [
            [
                InlineKeyboardButton(text="⬅️", callback_data=f"helps+{pos-1}"),
                InlineKeyboardButton(text="➡️", callback_data=f"helps+{pos+1}"),
            ],
        ]
    return button
