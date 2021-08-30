from os import path

from youtube_dl import YoutubeDL

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, download=True)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"🙅🏻 ᴠɪᴅᴇᴏ ʟᴇʙɪʜ ᴘᴀɴᴊᴀɴɢ ᴅᴀʀɪ {DURATION_LIMIT} ᴍᴇɴɪᴛ ᴛɪᴅᴀᴋ ᴅɪᴘᴇʀʙᴏʟᴇʜᴋᴀɴ,ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪsᴇᴅɪᴀᴋᴀɴ ᴀᴅᴀʟᴀʜ {duration} ᴍᴇɴɪᴛ)"
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"🙅🏻 ᴠɪᴅᴇᴏ ʟᴇʙɪʜ ᴘᴀɴᴊᴀɴɢ ᴅᴀʀɪ {DURATION_LIMIT} ᴍᴇɴɪᴛ ᴛɪᴅᴀᴋ ᴅɪᴘᴇʀʙᴏʟᴇʜᴋᴀɴ,ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪsᴇᴅɪᴀᴋᴀɴ ᴀᴅᴀʟᴀʜ {duration} ᴍᴇɴɪᴛ)"
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
