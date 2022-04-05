from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/cbe826936d4de9ec1838a.jpg",
                caption="✨ **ALBY-Userbot Berhasil Diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 9.0@ALBY-Userbot\n➠ **Ketik** `.ping` **Untuk Mengecek Bot**\n➠ **Ketik** `.help` **Untuk Melihat Informasi Module**\n━━━━━━━━━━━\n➠ **Powered By:** **✨ ᴀʟʙʏ ᴜꜱᴇʀʙᴏᴛ ✨**",
                buttons=[(Button.url("ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/ruangdiskusikami"),
                buttons=[(Button.url("ᴄʜᴀɴɴᴇʟ ᴜᴘᴅᴀᴛᴇꜱ", "https://t.me/ruangprojects"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
