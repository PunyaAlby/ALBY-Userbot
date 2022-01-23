import asyncio
import random
from userbot.events import register

APAKAH_STRING = ["Iya",
                 "Tidak",
                 "Mungkin",
                 "Bisa jadi",
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Pala bapak kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamak kau tu lah"
                 "Mungkin iya",
                 "Nggak tau",
                 "Benar",
                 "Aalah",
                 "Lu kali bukan dia",
                 "Apa iya",
                 "Kayaknya",
                 "Kayaknya sih",
                 "Ah masa",
                 "Masa sih",
                 "Oh gitu ya",
                 "Oh oke",
                 "Stres",
                 "Apasih",
                 "Gak jelas",
                 "Keren",
                 "Tolol",
                 "Anjing",
                 "Anjir",
                 "Goblok",
                 "Ganteng",
                 "Jelek",
                 "Bapakau",
                 "Dadjal",
                 "Setan",
                 "Iblis",
                 "Tidak perlu",
                 "Oh gitu",
                 "Tidak usah",
                 ]


@register(pattern="^apakah|Apakah ?(.*)")
async def apakah(event):
    await asyncio.sleep(0.5)
    await event.reply(random.choice(APAKAH_STRING))
