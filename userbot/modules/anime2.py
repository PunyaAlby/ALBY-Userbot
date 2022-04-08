# JANGAN HAPUS INI! © @JustRex
# Copyright Milik Xa-Userbot


import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import alby_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo


@alby_cmd(pattern="ppanime$")
async def _(event):
    try:
        ppanimenya = [
            ppanime
            async for ppanime in event.client.iter_messages(
                "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ppanimenya),
            caption=f"**nih pp anime buat** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**Lagi Ga Nemu pp anime!.**")


@alby_cmd(pattern="walanime$")
async def _(event):
    try:
        wallpapernya = [
            wallpaper
            async for wallpaper in event.client.iter_messages(
                "@Anime_WallpapersHD", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(wallpapernya),
            caption=f"**Anime Wallpaper By** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**Silahkan coba lagi.**")


@alby_cmd(pattern="shortanime$")
async def _(event):
    try:
        shortanimenya = [
            shortanime
            async for shortanime in event.client.iter_messages(
                "@anime_status998", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(shortanimenya),
            caption=f"**short anime video by** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**maaf lagi ga ada videonya, coba lagi deh.**")


CMD_HELP.update(
    {
        "tentanganime": f"❖ **Plugin : **`tentanganime`\
        \n\n ┌❖ **Perintah :** `.ppanime`\
        \n └❖ **Berfungsi : **untuk mendapatkan pp anime random.\
        \n\n ┌❖ **Perintah :** `.shortanime`\
        \n └❖ **Berfungsi : **Untuk Mendapatkan Video Anime Pendek untuk Status whatsapp.\
    "
    }
)

CMD_HELP.update(
    {
        "walpaperanime": f"❖ **Plugin : **`walpaperanime`\
        \n\n ┌❖ **Perintah :** `.walanime`\
        \n └❖ **Berfungsi : **Untuk Mendapatkan Wallpaper Aninme Random.\
    "
    }
)
