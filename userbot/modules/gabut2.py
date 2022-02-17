from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.albyy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Alby`")
    sleep(3)
    await typew.edit("`Umur kepo banget hmm`")
    sleep(3)
    await typew.edit("`sayang kamu💞`")
    sleep(1)
    await typew.edit("`Tinggal Di manapun yang membuat nyaman, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.nugas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai kamuu`")
    sleep(3)
    await typew.edit("`iyaa kamu yang baca😁`")
    sleep(3)
    await typew.edit("`semangat ya nugasnya✊🏻`")
    sleep(4)
    await typew.edit("`ingat masa depanmu lebih penting daripada capekmu hari ini ☺️`")
    sleep(3)
    await typew.edit("`SEMANGAT NUGASNYA CANTIK💞`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Albyy`\
    \n↳ : perkenalan Albyy\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.nugas`\
    \n↳ : Jan Lupa Semangat."
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.nugas`\
    \n↳ : Semangat nugas✊🏻."
})
