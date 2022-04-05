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

@alby_cmd(pattern="ppanime$")
async def _(event):
    try:
        ppanimenya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@CouplePFP", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ppanimenya),
            caption=f"Nih PP Animenya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Foto PP Anime nya.")

        
@alby_cmd(pattern="ppanime2$")
async def _(event):
    try:
        animeppnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@ppanimerandom", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(animeppnya),
            caption=f"Nih PP Animenya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Foto PP Anime nya.")


CMD_HELP.update(
    {
        "ppanime": f"❖ **Plugin : **`ppanime`\
        \n\n ┌❖ **Perintah :** `.ppanime`\
        \n └❖ **Berfungsi : **Untuk Mengirim Foto PP Anime couple secara random.\
        \n\n ┌❖ **Perintah :** `.ppanime1`\
        \n └❖ **Berfungsi : **Untuk Mengirim Foto PP Anime couple versi 2 secara random.\
    "
    }
)
