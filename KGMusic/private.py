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
        caption=f"""<b>ππππΎπππ ππ ππππ
πΉ α΄Κ Ι΄α΄α΄α΄ Ιͺs [{BOT_NAME}](https://t.me/{BOT_USERNAME})

β£οΈ {BOT_NAME} Can Run Tasks You Write In Death Note.</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β α΄α΄α΄Κα΄Κα΄α΄Ι΄ α΄α΄ Ι’Κα΄α΄α΄ β",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Ι’Κα΄α΄α΄", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton("α΄Κα΄Ι΄Ι΄α΄Κ", url=f"https://t.me/deathnotesupport"),
                ],
                [InlineKeyboardButton("γ­γ©Kira", url=f"https://t.me/{OWNER}"),
                ],
                [
                    InlineKeyboardButton(text="Κα΄Ι΄α΄α΄α΄Ι΄", callback_data="helps+1"),
                ],
            ]
        ),
    )


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7bf9f848e1c2edf2b8e33.jpg",
        caption=f"""<b>ππΉπΌπ³π¬πΊ π΅πΆπ»π¬ π©πΆπΆπ²π
1) Make γ­γ©Kira As Admin
2) Turn on Voice Chat
3) Write /userbotjoin in Death Note.
β’ If γͺγ₯γΌγ―Ryuk Joins, Enjoy Music.

Commands of All Death Note Owners
β’ /play (song title) β To Play the song you requested via YouTube
β’ /aplay (reply to audio) - To Play Song From Audio File
β’ /ytplay (song title) β To Play the song you requested via YouTube without any options
β’ /song (song title) - To Download songs from YouTube
β’ /vsong (video title) - To Download Videos on YouTube
β’ /search (song/video title) β To search for links on YouTube with details

Command all group admins
β’ /pause - To Pause Song playback
β’ /resume - To resume playback of the paused Song
β’ /skip - To Skip playback of the song to the next Song
β’ /end - To Stop Song playback
β’ /reload - To Refresh admin list</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Ι’Κα΄α΄α΄", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton("γ­γ©Kira", url=f"https://t.me/{OWNER}"),
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
        button = [[InlineKeyboardButton(text="π", callback_data="helps+2")]]
    elif pos == len(tr.HELPS_MSG) - 1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [[InlineKeyboardButton(text="π", callback_data=f"helps+{pos-1}")]]
    else:
        button = [
            [
                InlineKeyboardButton(text="π", callback_data=f"helps+{pos-1}"),
                InlineKeyboardButton(text="π", callback_data=f"helps+{pos+1}"),
            ],
        ]
    return button
