# Created by @punya_alby
# FROM ALBY-Userbot <https://github.com/PunyaAlby/ALBY-Userbot>
# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
# ⚠️ Do not remove credits ⚠️

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from userbot import CMD_HELP
from userbot.events import register

chat = "@awakmalas_bot"


@register(outgoing=True, pattern="^.rangkum ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("`Tambahin teks tugas kalian yang panjang agar dapat di ringkas`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/ringkas {text}")
            rangkum = await conv.get_response()
            await event.client.forward_messages(event.chat_id, rangkum)
            await event.delete()
        except YouBlockedUserError:
            await conv.send_message(f"/ringkas {text}")
            rangkum = await conv.get_response()
            await event.client.forward_messages(event.chat_id, rangkum)
            await event.delete()


CMD_HELP.update(
    {
        "rangkum": f"❖ **Plugin : **`rangkuman teks`\
        \n\n ┌❖ **Perintah :** `.rangkum <text>`\
        \n └❖ **Berfungsi : **membuat rangkuman tugas kamu yang panjang menjadi singkat.\
     "
    }
)
