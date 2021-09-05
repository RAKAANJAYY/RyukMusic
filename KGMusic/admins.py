from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from cache.admins import set
from callsmusic import callsmusic
from config import que, admins as a
from config import BOT_USERNAME
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command, other_filters


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def update_admin(client, message):
    global a
    admins = await client.get_chat_members(message.chat.id, filter="administrators")
    new_ads = []
    for u in admins:
        new_ads.append(u.user.id)
    a[message.chat.id] = new_ads
    await message.reply_text(
        "👹 **リュークRyuk Reload Successful!**\n\n• **Death Note Has Been Updated.**"
    )


@Client.on_message(command(["pause", f"pause@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (message.chat.id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[message.chat.id] == "paused"
    ):
        await message.reply_text("👹 **I Can't Find Something In Death Noter!**")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(
            "**👹 リュークRyuk  Pausing Song.**\n\n• To continue playback, write /resume in Death Note."
        )


@Client.on_message(command(["resume", f"resume@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (message.chat.id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[message.chat.id] == "playing"
    ):
        await message.reply_text("👹 **I Can't Find Something In Death Noter!**")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(
            "**👹 リュークRyuk Resume Song Playback**\n\n• To End, Write /end in Death Note"
        )


@Client.on_message(command(["end", f"end@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("👹 **I Can't Find Something In Death Noter!**")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("**👹 リュークRyuk Has Disconnected From Chat.**")


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("👹 **I Can't Find Something In Death Noter!**")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id, callsmusic.queues.get(message.chat.id)["file"]
            )
    qeue = que.get(message.chat.id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(
        f"**👹 リュークRyuk Passing The Target**\n**▶️ Next Goal:** {qeue[0][0]}"
    )
