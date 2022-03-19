# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Modifikasi by : @Punya_Alby

# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
# PERSETAN DENGAN ORANG YANG HAPUS CREDIT

""" Userbot help command """

from userbot import CMD_HANDLER as cmd
from userbot import ALIVE_NAME, CMD_HELP, bot
from userbot.utils import edit_delete, edit_or_reply, kyy_cmd

modules = CMD_HELP


@kyy_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    """For help command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, f"𝘔𝘢𝘢𝘧 𝘔𝘰𝘥𝘶𝘭𝘦 `{args}` 𝘛𝘪𝘥𝘢𝘬 𝘋𝘢𝘱𝘢𝘵 𝘋𝘪𝘵𝘦𝘮𝘶𝘬𝘢𝘯!!")
    else:
        user = await bot.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ❖  "
        await edit_or_reply(
            event,
            f"**❖ Daftar Perintah Untuk [ALBY-Userbot](https://github.com/PunyaAlby/ALBY-Userbot)**\n"
            f"**❖ Jumlah:** `{len(modules)}` **Modules**\n"
            f"**❖ Owner:** {ALIVE_NAME}\n"
            f"**❖ GUNAKAN DENGAN BIJAK :**\n\n 卍═❖• **DAFTAR MODULES** •❖═卍\n\n"
            f"**❖ {string}\n\n 卍══❖• **ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ** •❖══卍\n\nGroup Support @ruangdiskusikami\n\n"
        )
        await event.reply(
            f"╭┄──────┈┄┈──────┄\n"
            f"│ ❖ **Daftar Perintah ALBY USERBOT :**\n"
            f"│ ❖ **Jumlah** `{len(modules)}` **Modules**\n"
            f"│ ❖ **Owner:** [{user.first_name}](tg://user?id={user.id})\n"
            f"├┄──────┈┈──────┄\n"
            f"│ ❖ **Contoh Ketik** `{cmd}help ping`\n"
            f"│ ❖ **Untuk Melihat Informasi Module**\n"
            f"│ ❖ **Silahkan Ketik** `.helpme`\n" 
            f"├┄─────┈┄┈─────┄\n"
            f"│ ❖ **Jangan Lupa Berdoa** 🥰\n"
            f"╰┄──────┈┈──────┄"
        )
