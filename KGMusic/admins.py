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
        "✅ Bot reloaded correctly!\n\n• The Admin list has been updated."
    )


@Client.on_message(command(["pause", f"pause@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (message.chat.id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[message.chat.id] == "paused"
    ):
        await message.reply_text("📛 **No song is playing!**")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(
            "**⏸️ Music paused!**\n\n💡 For resuming the song, use command » /resume"
        )


@Client.on_message(command(["resume", f"resume@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (message.chat.id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[message.chat.id] == "playing"
    ):
        await message.reply_text("📛 **Can't find the currently paused song!**")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(
            "**⚡ Music resumed!**\n\n💡 For end the song, use command » /end"
        )


@Client.on_message(command(["end", f"end@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("📛 **No song is playing!**")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("**✅ Streaming ended**\n\n• Assistant has been disconnected from voice chat group")


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("📛 **No songs in queue!**")
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
        f"**💡 You jump to the next song queue..**\n┈┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┈**\n➠ skipped :** {skip[0]}\n**⚡ now playing :** {qeue[0][0]}"
    )
