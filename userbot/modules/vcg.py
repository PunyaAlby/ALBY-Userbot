# Thanks Full To Team Ultroid
# Fiks By ALBY @Punya_Alby


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import ALBY_cmd

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(ALBY):
    ALBY = await ALBY.client(getchat(ALBY.chat_id))
    await ALBY.client(getvc(ALBY.full_chat.call, limit=1))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@ALBY_cmd(pattern="startvc$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("`Memulai Obrolan Suara`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@ALBY_cmd(pattern="stopvc$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Mematikan Obrolan Suara`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@ALBY_cmd(pattern="vcinvite")
async def _(ALBY):
    await ALBY.edit("`Sedang Menginvite Member...`")
    users = []
    z = 0
    async for x in ALBY.client.iter_participants(ALBY.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await ALBY.client(invitetovc(call=await get_call(ALBY), users=p))
            z += 6
        except BaseException:
            pass
    await ALBY.edit(f"`Menginvite {z} Member`")


CMD_HELP.update(
    {
        "vcg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vcinvite`\
         \n↳ : Invite semua member yang berada di group."
    }
)
