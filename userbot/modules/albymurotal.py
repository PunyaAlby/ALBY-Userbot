# Created by @punya_alby
# FROM ALBY-Userbot <https://github.com/PunyaAlby/ALBY-Userbot>
# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
# ⚠️ Do not remove credits ⚠️

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import alby_cmd
import random
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo


@alby_cmd(pattern="murotalvideo$")
async def _(event):
    try:
        videonya = [
            video
            async for video in event.client.iter_messages(
                "@vidgram_murotal", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(videonya),
            caption=f" Nih Kak Video Murotal nya 😎",
        )
        await event.delete()
    except Exception:
        await event.edit("Murotal Video nya Tidak ditemukan Karena Kamu belum wudhu _-.")


@alby_cmd(pattern="murotal$")
async def _(event):
    try:
        imagenya = [
            image
            async for image in event.client.iter_messages(
                "@vidgram_murotal", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(imagenya),
            caption=f" Nih Kak Gambar Murotal nya 😎",
        )
        await event.delete()
    except Exception:
        await event.edit("Gambar Murotal nya Tidak ditemukan Karena Kamu belum wudhu _-.")


CMD_HELP.update(
    {
        "murotalvideo": f"❖ **Plugin : **`Murotal Video`\
        \n\n ┌❖ **Perintah :** `.murotalvideo`\
        \n └❖ **Berfungsi : **Untuk Mencari video murotal secara random.\
    "
    }
)

CMD_HELP.update(
    {
        "murotal": f"❖ **Plugin : **`Murotal`\
        \n\n ┌❖ **Perintah :** `.murotal`\
        \n └❖ **Berfungsi : **Untuk Mencari gambar berisi kata kata murotal secara random.\
    "
    }
)
