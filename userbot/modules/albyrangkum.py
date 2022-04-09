# Created by @punya_alby
# FROM ALBY-Userbot <https://github.com/PunyaAlby/ALBY-Userbot>
# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
# ⚠️ Do not remove credits ⚠️

import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.rangkum(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin teks tugas kalian yang panjang agar dapat di ringkas`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_rangkum = await conv.send_message(f"/ringkas {text}")
            rangkum = await conv.get_response()
            response = await conv.get_response()
            """ - don't spam notif - """
            await event.client.forward_messages(event.chat_id, rangkum)
            await event.client.forward_messages(event.chat_id, response)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await event.reply(
            f"╭╌╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╌╮\n"
            f"┊ ▸ **Rangkuman by** ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ\n"
            f"┊ ▸ **[ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ]**(https://t.me/ruangdiskusikami)\n"
            f"┊ ▸ **[ᴄʜᴀɴɴᴇʟ ᴜᴘᴅᴀᴛᴇꜱ]**(https://t.me/ruangprojects)\n"
            f"╰╌╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╌╯")
        await event.client.delete_messages(conv.chat_id, [msg_rangkum.id, rangkum.id, response.id])
        await event.delete()

CMD_HELP.update(
    {
        "rangkuman": f"❖ **Plugin : **`rangkum tugas`\
        \n\n ┌❖ **Perintah :** `.rangkum <text>`\
        \n └❖ **Berfungsi : **Untuk Merangkum atau Meringkas Tugas yang Panjang.\
    "
    }
)
