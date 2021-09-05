from os import path

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import converter
from callsmusic import callsmusic, queues
from config import BOT_IMAGE as bi
from config import DURATION_LIMIT, OWNER, SUPPORT_GROUP
from downloaders import youtube
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.filters import command, other_filters
from helpers.gets import get_file_name, get_url


@Client.on_message(command("aplay") & other_filters)
@errors
async def aplay(_, message: Message):

    lel = await message.reply("🔁 **リュークRyuk Processing Audio...**")
    message.from_user.id
    message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"),
                InlineKeyboardButton("キラKira", url=f"https://t.me/{OWNER}"),
            ]
        ]
    )

    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"👹 **リュークRyuk Cannot Play More Than** {DURATION_LIMIT} !"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("👹 **You Didn't Write Something On The Death Note!**")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await lel.edit(f"🔢 **Queue In Position** {position}!")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
            photo=f"{bi}",
            reply_markup=keyboard,
            caption="🖋️ **Running Tasks From** {}!".format(
                message.from_user.mention()
            ),
        )
        return await lel.delete()
