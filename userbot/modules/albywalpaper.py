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
from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos


@alby_cmd(pattern="walaesthetic$")
async def _(event):
    try:
        walpapernya = [
            walpaper
            async for walpaper in event.client.iter_messages(
                "@walpaper_aestetic", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(walpapernya),
            caption=f" Nih Kak Walpaper Aesthetic nya [{owner}](tg://user?id={aing.id}) 😎",
        )
        await event.delete()
    except Exception:
        await event.edit("Walpapernya nya Tidak ditemukan Karena Kamu belum mandi _-.")


@alby_cmd(pattern="walbts$")
async def _(event):
    try:
        walpapernya = [
            walpaper
            async for walpaper in event.client.iter_messages(
                "@walpaperbts", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(walpapernya),
            caption=f" Nih Kak Walpaper BTS nya [{owner}](tg://user?id={aing.id}) 😎",
        )
        await event.delete()
    except Exception:
        await event.edit("Walpapernya nya Tidak ditemukan Karena Kamu terlalu fanatik _-.")


CMD_HELP.update(
    {
        "walpaperaesthetic": f"❖ **Plugin : **`walpaper aesthetic`\
        \n\n ┌❖ **Perintah :** `.walaesthetic`\
        \n └❖ **Berfungsi : **Untuk Mencari WALPAPER AESTHETIC secara random.\
    "
    }
)

CMD_HELP.update(
    {
        "walpaperbts": f"❖ **Plugin : **`walpaper bts`\
        \n\n ┌❖ **Perintah :** `.walbts`\
        \n └❖ **Berfungsi : **Untuk Mencari WALPAPER BTS secara random.\
    "
    }
)
