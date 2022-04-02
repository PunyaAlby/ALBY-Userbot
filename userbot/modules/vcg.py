# Thanks Full To Team Ultroid
# Fiks By ALBY @punya_alby


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl import types
from telethon.utils import get_display_name

from userbot import ALIVE_NAME
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_delete, edit_or_reply, alby_cmd
from userbot.events import register

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(alby):
    alby = await alby.client(getchat(alby.chat_id))
    await alby.client(getvc(alby.full_chat.call, limit=1))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@alby_cmd(pattern="startvc$")
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Memulai Obrolan Suara`")
    except Exception as ex:
        await edit_or_reply(c, f"**ERROR:** `{ex}`")


@alby_cmd(pattern="stopvc$")
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Mematikan Obrolan Suara`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@alby_cmd(pattern="vcinvite")
async def _(alby):
    await edit_or_reply(alby, "`Sedang Menginvite Member...`")
    users = []
    z = 0
    async for x in alby.client.iter_participants(alby.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await alby.client(invitetovc(call=await get_call(alby), users=p))
            z += 6
        except BaseException:
            pass
    await edit_or_reply(alby, f"`Menginvite {z} Member`")


@alby_cmd(pattern="vctitle(?: |$)(.*)")
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")

@alby_cmd(pattern="joinvc(?: |$)(.*)")
async def join_(event):
    xnxx = await edit_or_reply(event, f"**Processing**")
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client(GetFullUserRequest(chat))
        except Exception as e:
            await edit_delete(event, f"**ERROR:** `{e}`", 30)
    else:
        chat = event.chat_id
        vcmention(event.sender)
    if not call_py.is_connected:
        await call_py.start()
    await call_py.join_group_call(
        chat,
        AudioPiped("http://duramecho.com/Misc/SilentCd/Silence01s.mp3"),
        stream_type=StreamType().pulse_stream,
    )
    try:
        await xnxx.edit("**{}** `Joined VC in` `{}`".format(ALIVE_NAME, str(event.chat_id)))
    except Exception as ex:
        await edit_delete(event, f"**ERROR:** `{ex}`")


@alby_cmd(pattern="leavevc(?: |$)(.*)")
async def leavevc(event):
    """leave video chat"""
    xnxx = await edit_or_reply(event, "Processing")
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if from_user:
        try:
            await call_py.leave_group_call(chat_id)
        except (NotInGroupCallError, NoActiveGroupCall):
            pass
        await xnxx.edit(
            "**{}** `Left the voice in` `{}`".format(ALIVE_NAME, str(event.chat_id))
        )
    else:
        await edit_delete(event, f"**Maaf {ALIVE_NAME} Tidak di VCG**")


CMD_HELP.update(
    {
        "vcg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vctittle <tittle vcg>`\
         \n↳ : `Mengubah tittle/judul Obrolan Suara.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite semua member yang berada di group."
    }
)

CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
      \n\n  •  **Syntax :** `{cmd}joinvc`\
      \n  •  **Function :** Melakukan Fake OS.\
      \n\n  •  **Syntax :** `{cmd}leavevc`\
      \n  •  **Function :** Memberhentikan Fake OS.\
      "
    }
)
