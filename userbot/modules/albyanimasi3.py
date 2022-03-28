from time import sleep
from userbot import ALIVE_NAME, CMD_HELP, GROUP_LINK, bot
from userbot.events import register
from telethon import events
import asyncio

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname()
# ============================================

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "fadmin":

        await event.edit(input_str)

        animation_chars = [

            "**Promoting User As Admin...**",
            "**Enabling All Permissions To User...**",
            "**(1) Send Messages: ☑️**",
            "**(1) Send Messages: ✅**",
            "**(2) Send Media: ☑️**",
            "**(2) Send Media: ✅**",
            "**(3) Send Stickers & GIFs: ☑️**",
            "**(3) Send Stickers & GIFs: ✅**",
            "**(4) Send Polls: ☑️**",
            "**(4) Send Polls: ✅**",
            "**(5) Embed Links: ☑️**",
            "**(5) Embed Links: ✅**",
            "**(6) Add Users: ☑️**",
            "**(6) Add Users: ✅**",
            "**(7) Pin Messages: ☑️**",
            "**(7) Pin Messages: ✅**",
            "**(8) Change Chat Info: ☑️**",
            "**(8) Change Chat Info: ✅**",
            "**Permission Granted Successfully**",
            "**pRoMooTeD SuCcEsSfUlLy**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 17)

    input_str = event.pattern_match.group(1)

    if input_str == "fleave":

        await event.edit(input_str)

        animation_chars = [

            "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
            "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
            "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "**Chat Message Exported To** `./Inpu/`",
            "**Chat Message Exported To** `./Inpu/homework/`",
            "**Chat Message Exported To** `./Inpu/homework/groupchat.txt`",
            "__Legend is leaving this chat.....! Bye geys..__",
            "__Legend is leaving this chat.....! Bye geys..__"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 17])


@register(outgoing=True, pattern='^.gbn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kita Gban Jamet duls!!...`")
    sleep(1)
    await typew.edit("`Memulai global banned...✅`")
    sleep(2)
    await typew.edit("`Proses Global banned...✅`")
    sleep(3)
    await typew.edit(f"╭✠╼━━━━━━❖━━━━━━━✠\n┣• **TUAN:** `{ALIVE_NAME}`\n┣• **GBAN BERHASIL..!**\n┣• **Aksi:** `LAGI GABUT MAU GBAN AJA`\n┣• **KENYATAAN NYA:** `TAPI BOHONG 🤣🤣 GBAN PALSU INI🤣`\n╰✠╼━━━━━━❖━━━━━━━✠")

@register(outgoing=True, pattern='^.gkck(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Proses global kick Si ngentot!!...**")
    sleep(3)
    await typew.edit("__mengeluarkan dari (1) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (2) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (3) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (4) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (5) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (6) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (7) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (8) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (9) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (10) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (11) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (12) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (13) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (14) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (15) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (16) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (17) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (18) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (19) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (20) Group__")
    sleep(2)
    await typew.edit("**Pengguna berhasil di kick global dari (20) obrolan dalam grup.**")
    sleep(2)
    await typew.edit(f"╭✠╼━━━━━━❖━━━━━━━✠\n┣• **TUAN:** `{ALIVE_NAME}`\n┣• **GBAN BERHASIL..!**\n┣• **Aksi:** `LAGI GABUT MAU Global Kick AJA`\n┣• **KENYATAAN NYA:** `TAPI BOHONG 🤣🤣 Gkick PALSU INI🤣`\n╰✠╼━━━━━━❖━━━━━━━✠")



@register(outgoing=True, pattern='^.gmt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Memulai proses Global mute...`")
    sleep(3)
    await typew.edit("`Pengguna berhasil di Global mute...!`")
    sleep(2)
    await typew.edit(f"╭✠╼━━━━━━❖━━━━━━━✠\n┣• **TUAN:** `{ALIVE_NAME}`\n┣• **GBAN BERHASIL..!**\n┣• **Aksi:** `LAGI GABUT MAU Global Mute AJA`\n┣• **KENYATAAN NYA:** `TAPI BOHONG 🤣🤣 Gmute PALSU INI🤣`\n╰✠╼━━━━━━❖━━━━━━━✠")


@register(outgoing=True, pattern='^.fdyno(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Memeriksa dyno heroku anda...`")
    sleep(1)
    await typew.edit("✨")
    sleep(2)
    await typew.edit(f"𝗜𝗡𝗙𝗢 𝗞𝗘𝗞𝗨𝗔𝗧𝗔𝗡!! {REPO_NAME}\n\n"
                     "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                     "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗦𝗔𝗔𝗧 𝗜𝗡𝗜 :\n"
                     "┣• ▸ 999 ᴊᴀᴍ - 999 ᴍᴇɴɪᴛ.\n" 
                     "┣• ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : 999%\n" 
                     "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                     "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
                     "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                     "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗕𝗨𝗟𝗔𝗡 𝗜𝗡𝗜 :\n"
                     "┣• ▸ `999999` ᴊᴀᴍ - `999999` ᴍᴇɴɪᴛ.\n"
                     "┣• ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : 1000%.\n"
                     "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                     f"𝗣𝗘𝗠𝗜𝗟𝗜𝗞  : {ALIVE_NAME}\n"
                     f"**•JOIN•** : [MY GROUP]({GROUP_LINK})")


@register(outgoing=True, pattern='^.kickme(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"`{ALIVE_NAME}, Saat Nya Pergi...`")
    sleep(3)
    await typew.edit(f"`{ALIVE_NAME} Telah meninggalkan Group....`")


@register(outgoing=True, pattern='^.fck(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".                       /¯ )")
    await typew.edit(".                       /¯ )\n                      /¯  /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")


CMD_HELP.update(
    {
        "animasi5": f"❖ **Plugin : **`animasi5`\
        \n\n ┌❖ **Perintah :** `.fadmin`\
        \n └❖ **Berfungsi : **Mengirim animasi menjadi admin bohongan.\
        \n\n ┌❖ **Perintah :** `.fleave`\
        \n └❖ **Berfungsi : **Mengirim animasi keluar group bohongan.\
        \n\n ┌❖ **Perintah :** `.gbn`\
        \n └❖ **Berfungsi : **Mengirim animasi gban target bohongan.\
        \n\n ┌❖ **Perintah :** `.gmt`\
        \n └❖ **Berfungsi : **Mengirim animasi global mute target bohongan.\
        \n\n ┌❖ **Perintah :** `.gkck`\
        \n └❖ **Berfungsi : **Mengirim animasi global kick bohongan.\
        \n\n ┌❖ **Perintah :** `.fdyno`\
        \n └❖ **Berfungsi : **Mengirim animasi jumlah dyno palsu.\
        \n\n ┌❖ **Perintah :** `.kickme`\
        \n └❖ **Berfungsi : **Mengirim animasi keluar group beneran.\
    "
    }
)
