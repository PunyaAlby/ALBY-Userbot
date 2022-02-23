from platform import uname
from time import sleep

from userbot import ALIVE_NAME, CMD_HELP, WEATHER_DEFCITY
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG LAH GOBLOKK!!!**")


# Pantun


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@register(outgoing=True, pattern="^.albykenalan(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Hai Kamuu👋`")
    sleep(2)
    await typew.edit("`kata pepatah : Tak kenal maka tak sayang`")
    sleep(1)
    await typew.edit("`yaudah kita kenalan, biar bisa saling sayang💞`")
    sleep(2)
    await typew.edit("`Perkenalkan Namaku Alby✨`")
    sleep(1)
    await typew.edit("`umur doain aja semoga awet muda`")
    sleep(2)
    await typew.edit("`Tinggal Di manapun yang menurut ku nyaman`")
    sleep(1)
    await typew.edit("`salam kenal ya☺️`")
    sleep(2)
    await typew.edit("`udah gitu dulu ya..`")
    sleep(1)
    await typew.edit(
        "`⚡ Semoga perkenalan kita bisa membuat kita saling sayang satu sama lain☺️`"
    )


# King Userbot Support


@register(outgoing=True, pattern="^.istighfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@register(outgoing=True, pattern=r"^\.virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


@register(outgoing=True, pattern="^.perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(1.5)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")


# Perkenalan


@register(outgoing=True, pattern="^.albyy(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Sih alby kan nakal bangeeettt😂**")
    sleep(1)
    await typew.edit("**Ehh Gak Bercanda Deh😁**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Alby emang nakal🤭**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Alby Kan baik, Ganteng, pokoknya idaman banget😄**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Alby Nangis Minta pelmen😂**")
    sleep(1)
    await typew.edit("**Maaf Ya Alby Ganteng Bercanda😁**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")


# Create by myself @skyzuex


@register(outgoing=True, pattern="^.nugas(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Kamu👋`")
    sleep(2)
    await event.edit(f"`iyaa kamuu, yang baca😁`")
    sleep(1.5)
    await event.edit("`semangat ya nugasnya✊🏻`")
    sleep(2)
    await event.edit("`nda boleh malas malas😤`")
    sleep(2)
    await event.edit("`SEMANGAT💞💞💞`")


# Nugas


@register(outgoing=True, pattern="^.kerja(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Kamu👋`")
    sleep(2)
    await event.edit(f"`iyaa kamuu, yang baca😁`")
    sleep(1.5)
    await event.edit("`semangat ya kerjanya✊🏻`")
    sleep(2)
    await event.edit("`nda boleh malas malas😤`")
    sleep(2)
    await event.edit("`SEMANGAT💞💞💞`")


# Kerja


@register(outgoing=True, pattern="^.prenjon(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai you👋`")
    sleep(2)
    await event.edit(f"`iyaa kamuu..`")
    sleep(2)
    await event.edit("`Mau bilang sesuatu ni..`")
    sleep(2)
    await event.edit("`Sebenarnya..`")
    sleep(2)
    await event.edit("`Sebenarnya gua suka sama lu`")
    sleep(2)
    await event.edit("`Tapi lu nya ga suka sama gua😟`")
    sleep(2)
    await event.edit("`Tapi gapapa🙂`")
    sleep(2)
    await event.edit("`i'm okay😌`")


# prenjon


@register(outgoing=True, pattern="^.kangencerita(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai kamu👋`")
    sleep(2)
    await event.edit(f"`apa kabar?`")
    sleep(2)
    await event.edit("`makan nya udah?`")
    sleep(2)
    await event.edit("`buat hari ini gimana?`")
    sleep(2)
    await event.edit("`ada yang mau kamu ceritain ngga?`")
    sleep(2)
    await event.edit("`kalau ada sini cerita sini sama aku🥺`")
    sleep(2)
    await event.edit("`aku kangen kamu ceritaa🥺`")
    sleep(2)
    await event.edit("`aku siap jadi pendengar cerita kamu`")


# KangenCerita



CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Mengucapkan Salam\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.istighfar`\
        \nUsage : Untuk Mengucapkan istighfar\
        \n\n Cmd : `.virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `.perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.albyy`\
        \nUsage : buat ngeledek albyy\
        \n\n Cmd : `.nugas`\
        \nUsage : semangatin orang ngerjain tugas\
        \n\n Cmd : `.kerja`\
        \nUsage : semangatin orang bekerja\
        \n\n Cmd : `.prenjon`\
        \nUsage : Cinta friendzone\
        \n\n Cmd : `.kangencerita`\
        \nUsage : Kangen cerita dari kamu\
    "
    }
)
