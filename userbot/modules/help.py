# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Command` **Tidak Valid**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ❖  "
        await event.edit("**✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨**\n\n"
                         f"**❖ 𝙿𝙴𝙼𝙸𝙻𝙸𝙺 𝙱𝙾𝚃 : {DEFAULTUSER}**\n**{EMOJI_HELP}  𝙼𝙾𝙳𝚄𝙻𝙴𝚂 : {len(modules)}**\n\n"
                         f"**❖ 𝚂𝙴𝙼𝚄𝙰 𝙼𝙴𝙽𝚄 :**\n\n 卍═════❖•ೋ° **(っ◔◡◔)っ 🌙** °ೋ•❖═════卍\n\n"
                         f"❖ {string}\n\n 卍═════❖•ೋ° **(っ◔◡◔)っ 🌙** °ೋ•❖═════卍\n\nSupport @ruangdiskusikami\n\n")
        await rambot.reply(f"\n**Contoh** : Ketik <`.help ping`> Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha..")
        await asyncio.sleep(1000)
        await event.delete()
