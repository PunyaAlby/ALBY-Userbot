# Copyright (C) 2020 TeamDerUntergang.
# SedenUserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# ALBYUSERBOT
# SedenUserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modifikasi by : @Punya_Alby

# ░█████╗░██╗░░░░░██████╗░██╗░░░██╗
# ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝
# ███████║██║░░░░░██████╦╝░╚████╔╝░
# ██╔══██║██║░░░░░██╔══██╗░░╚██╔╝░░
# ██║░░██║███████╗██████╦╝░░░██║░░░
# ╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░

# PERSETAN DENGAN ORANG YANG HAPUS CREDIT

import asyncio
import sys

from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HANDLER as cmd
from userbot import BOT_USERNAME, bot
from userbot.utils import edit_or_reply, kyy_cmd
from userbot.utils import autoinlinebot


@kyy_cmd(pattern="helpme")
async def _(event):
    if event.fwd_from:
        return
    if BOT_USERNAME is not None:
        chat = "@Botfather"
        try:
            results = await event.client.inline_query(BOT_USERNAME, "@ALBYUserbot")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            xx = await edit_or_reply(
                event,
                "**Inline Mode Tidak aktif.**\n__Sedang Menyalakannya, Harap Tunggu Sebentar...__\nKalau sudah 3 menit tidak ada perubahan silahkan pergi ke bot @BotFather ketikan /mybots\nKemudian pilih bot Assistant mu yang ada di group log\nLalu pilih Bot Settings > Pilih inline Mode > pilih Turn on\nPergi ke group log lagi dan Ketik** `{cmd}helpme` **lagi untuk membuka menu bantuan modules nya",
            )
            bot.loop.run_until_complete(autoinlinebot())
            xx = await xx.edit(
                    f"**BERHASIL MENYALAKAN MODE INLINE**\n\n**Ketik** `{cmd}helpme` **lagi untuk membuka menu bantuan.**"
            )
