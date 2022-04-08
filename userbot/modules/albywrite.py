# Created by @punya_alby
# FROM ALBY-Userbot <https://github.com/PunyaAlby/ALBY-Userbot>
# ALBY GANTENG
# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
# ⚠️ Do not remove credits ⚠️

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.nulis(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas1 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis1(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas2 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis2(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas7 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis3(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas8 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis4(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas1 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis5(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas2 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis6(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas7 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis7(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 3")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas8 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis8(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas1 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis9(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas2 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis10(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas7 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()

@register(outgoing=True, pattern=r"^\.nulis11(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Tambahin Tulisan yang mau dibuat`")
    else:
        await event.edit("`Processing..`")
    chat = "@awakmalas_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 5")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas8 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            nulis,
            caption=f"TULISAN by [✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨](https://t.me/ruangprojects/82)",
        )
        await event.client.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await event.delete()


CMD_HELP.update(
    {
        "nulis": f"❖ **Plugin : **`nulis`\
        \n\n ┌❖ **Perintah :** `.nulis <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas pertama dengan font 1.\
        \n\n ┌❖ **Perintah :** `.nulis1 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di beda kertas kedua dengan font 1.\
        \n\n ┌❖ **Perintah :** `.nulis2 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di beda kertas ketiga dengan font 1.\
        \n\n ┌❖ **Perintah :** `.nulis3 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di beda kertas keempat dengan font 1.\
    "
    }
)

CMD_HELP.update(
    {
        "nulis2": f"❖ **Plugin : **`nulis kedua`\
        \n\n ┌❖ **Perintah :** `.nulis4 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas pertama dengan font 2.\
        \n\n ┌❖ **Perintah :** `.nulis5 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas kedua dengan font 2.\
        \n\n ┌❖ **Perintah :** `.nulis6 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas ketiga dengan font 2.\
        \n\n ┌❖ **Perintah :** `.nulis7 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas keempat dengan font 2.\
    "
    }
)

CMD_HELP.update(
    {
        "nulis3": f"❖ **Plugin : **`nulis ketiga`\
        \n\n ┌❖ **Perintah :** `.nulis8 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas pertama dengan font 3.\
        \n\n ┌❖ **Perintah :** `.nulis9 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas kedua dengan font 3.\
        \n\n ┌❖ **Perintah :** `.nulis10 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas ketiga dengan font 3.\
        \n\n ┌❖ **Perintah :** `.nulis11 <text>`\
        \n └❖ **Berfungsi : **membuat tulisan online di kertas keempat dengan font 3.\
    "
    }
)
