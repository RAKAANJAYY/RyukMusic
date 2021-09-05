from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import ASSISTANT_NAME as an
from config import BOT_IMAGE, BOT_NAME, BOT_USERNAME, OWNER, SUPPORT_GROUP
from KGMusic.msg import Messages as tr
from helpers.filters import command


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7bf9f848e1c2edf2b8e33.jpg",
        caption=f"""<b>𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙃𝙀𝙇𝙇
👹 ᴍʏ ɴᴀᴍᴇ ɪs [{BOT_NAME}](https://t.me/{BOT_USERNAME})

✣️ {BOT_NAME} Can Run Tasks You Write In Death Note.</b>""",
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
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/deathnotesupport"),
                ],
                [InlineKeyboardButton("キラKira", url=f"https://t.me/{OWNER}"),
                ],
                [
                    InlineKeyboardButton(text="ʙᴀɴᴛᴜᴀɴ", callback_data="helps+1"),
                ],
            ]
        ),
    )


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7bf9f848e1c2edf2b8e33.jpg",
        caption=f"""<b>📖𝑹𝑼𝑳𝑬𝑺 𝑵𝑶𝑻𝑬 𝑩𝑶𝑶𝑲📖
1) Make キラKira As Admin
2) Turn on Voice Chat
3) Write /userbotjoin in Death Note.
• If リュークRyuk Joins, Enjoy Music.

Commands of All Death Note Owners
• /play (song title) — To Play the song you requested via YouTube
• /aplay (reply to audio) - To Play Song From Audio File
• /ytplay (song title) — To Play the song you requested via YouTube without any options
• /song (song title) - To Download songs from YouTube
• /vsong (video title) - To Download Videos on YouTube
• /search (song/video title) – To search for links on YouTube with details

Command all group admins
• /pause - To Pause Song playback
• /resume - To resume playback of the paused Song
• /skip - To Skip playback of the song to the next Song
• /end - To Stop Song playback
• /reload - To Refresh admin list</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton("キラKira", url=f"https://t.me/{OWNER}"),
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
        button = [[InlineKeyboardButton(text="👉", callback_data="helps+2")]]
    elif pos == len(tr.HELPS_MSG) - 1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [[InlineKeyboardButton(text="👈", callback_data=f"helps+{pos-1}")]]
    else:
        button = [
            [
                InlineKeyboardButton(text="👈", callback_data=f"helps+{pos-1}"),
                InlineKeyboardButton(text="👉", callback_data=f"helps+{pos+1}"),
            ],
        ]
    return button
