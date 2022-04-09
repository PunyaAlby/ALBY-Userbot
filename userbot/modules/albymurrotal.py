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
from telethon.tl.types import InputMessagesFilterAudio


@alby_cmd(pattern="murotal$")
async def _(event):
    try:
        murotalnya = [
            murotal
            async for murotal in event.client.iter_messages(
                "@MurotalAnakJuz30", filter=InputMessagesFilterAudio
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(murotalnya),
            caption=f" Nih Kak Murotal nya 😎 [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Murotal nya Tidak ditemukan, mungkin karena kamu belum wudhu _-.")


CMD_HELP.update(
    {
        "murotal": f"❖ **Plugin : **`murotal juz 30`\
        \n\n ┌❖ **Perintah :** `.murotal`\
        \n └❖ **Berfungsi : **Untuk Mencari audio murotal juz 30 secara random.\
    "
    }
)
