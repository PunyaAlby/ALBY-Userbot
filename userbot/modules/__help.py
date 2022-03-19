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
                "**Inline Mode Tidak aktif.**\n__Sedang Menyalakannya, Harap Tunggu Sebentar...__",
            )

async def autobot():
    if who.username:
        username = who.username + "_ubot"
    else:
        username = "ALBY" + (str(who.id))[5:] + "ubot"
    bf = "@BotFather"
    await bot(UnblockRequest(bf))
    await bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await bot.send_message(bf, BOT_USERNAME)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    await bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "ALBY" + (str(who.id))[6:] + str(ran) + "ubot"
        await bot.send_message(bf, BOT_USERNAME)
        await asyncio.sleep(1)
        nowdone = (await bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
        await bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{BOT_USERNAME}")
        await asyncio.sleep(1)
        await bot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{BOT_USERNAME}")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"Managed With ☕️ By {who.first_name}")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{BOT_USERNAME}")
        await asyncio.sleep(1)
        await bot.send_message(
            bf, f"✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @ruangprojects ✨"
        )
        await bot.send_message(
            BOTLOG_CHATID,
            f"**BERHASIL MENYALAKAN MODE INLINE**",
        )
            sys.exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        await bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{BOT_USERNAME}")
        await asyncio.sleep(1)
        await bot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{BOT_USERNAME}")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"Managed With ☕️ By {who.first_name}")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{BOT_USERNAME}")
        await asyncio.sleep(1)
        await bot.send_message(
            bf, f"✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @ruangprojects ✨"
        )
        await bot.send_message(
            BOTLOG_CHATID,
            f"**BERHASIL MENYALAKAN MODE INLINE**",
        )
                await xx.edit(
                    f"**Berhasil Menyalakan Mode Inline**\n\n**Ketik** `{cmd}helpme` **lagi untuk membuka menu bantuan.**"
                )
            await bot.delete_messages(
                conv.chat_id,
                [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
            )
    else:
        await edit_or_reply(
            event,
            "**Silahkan Buat BOT di @BotFather dan Tambahkan Var** `BOT_TOKEN` & `BOT_USERNAME`",
        )
