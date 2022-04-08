# @JustRex
# Xa-Userbot
# Special Ramadhan
# recode by @greyyvbss

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, alby_cmd


@alby_cmd(pattern="puasa(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum kak ,Masih Semangat kan Puasanya?**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="puasa2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**ngabuburit yok!😁**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="puasa3(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Maap lagi ga mau gibah gua lagi puasa!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="puasa4(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Cihh Ganteng Doang, Puasa Kagak!!!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="puasa5(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Cieeeee Ga Puasa, dah gede jugak kalah sama adek gua lu**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="puasa6(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Bangga lo ga puasa? Gua sih Malu!!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="takjil(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Info Takjil Gratis Masseh, yang ada koleknya🥘!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="takjil2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Ada yang mau ikut gua nyari takjil ga 😁??**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="takjil3(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Gopudin makanan dong, Buat Buka puasa 🙃**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="ngaji(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Daripada War War Gajelas mending ngaji kak 😎**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="ngaji2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Gibah mulu lu, ngaji lah!!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sabar(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Sabar Aja, Kan lagi Puasa, abis buka baru kita hajar xixixi**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sabar2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Untung Lagi puasa jadinya gua Sabar**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="setan(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Gua ga gampang Kehasut Setan Kek lu 😏**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="setan2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Setan Kok Ngehasut Setan? Awikwok**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="setan3(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**CIE SETAN LAGI NGEGODA**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="s1(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Jum'atan dulu ah.... Mau Farming Sendal 🥿**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="s2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Sholat ah Biar Ganteng😎**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="s3(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Puasa doang, Sholat Kagak!!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sdkh(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Ga ada yang niat sedekah Ke Gua nih?**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sdkh2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Bagi duit dong buat beli baju Lebaran :)**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="warteg(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Info Warteg yang buka dong gaes!, Mau Nyemen nihh**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="warteg2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Warteg Depan Rumah lu buka ga? Nyemen Bareng Yukk**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="warteg3(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**WARTEG KUY!!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sahur(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**SAHUR WOIII SAHURRRR!!, BURUAN KEBURU IMSAK**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sahur2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Bagi Nasi kek, Mau Sahur Gada apa apa nih hmmm**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sahur3(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Ga semangat Puasanya, gara gara Ga dibangunin sahur sama ayang**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="buka(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Selamat Berbuka Puasa...😊**")


@alby_cmd(pattern="magrib(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Cieeee Lagi nungguin Adzan Magrib Ya wkwkw**")


@alby_cmd(pattern="bukber(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Ga ada niatan Bukber ni GC?**")


@alby_cmd(pattern="bukber2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Gausah sok ngajakin Bukber kalo ujung ujungnya cuma Wacana!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="bukbersad(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Mau Bukber sama Ayang tapi ga punya, dahlahhhhh**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="taraw1(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**TARAWEH GOBLOK!! JANGAN DITELE MULU**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="taraw2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**CONTOH ORANG ORANG TOLOL YANG GA TARAWEH DEMI WAR DI TELE!**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="nyemen(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Nyemen Dimana Ya Biar ga ketauan xixixi**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="nyemen2(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Nyemen Kuyyyyy**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()

@alby_cmd(pattern="nyemen3(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Temenin Gua Nyemen Di Warteg Kuyy, Tenang Gua Bayarin**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@alby_cmd(pattern="sholat(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**SHOLAT TOLOL! PERCUMA LO PUASA TAPI GA SHOLAT, NAHAN LAPER HAUS SIA SIA DOANG!! JANGAN MIKIRIN TELEGRAM TERUS, DI AKHIRAT GA BISA WAR SAMA MALAIKAT TOLOL!**")


CMD_HELP.update(
    {
        "ramadhan": f"**Plugin : **`ramadhan`\
        \n\n ┌❖ **Perintah:** `{cmd}puasa`\
        \n └❖ **Berfungsi : **Nanya Semangat ga puasanya ke orang, cobain aja jing.\
        \n\n ┌❖ **Perintah:** `{cmd}puasa2`\
        \n └❖ **Berfungsi : **Ngajak Ngabuburit.\
        \n\n ┌❖ **Perintah:** `{cmd}puasa3`\
        \n └❖ **Berfungsi : **Ga mau Gibah.\
        \n\n ┌❖ **Perintah:** `{cmd}puasa4`\
        \n └❖ **Berfungsi : **Ganteng doang, Puasa kaga!.\
        \n\n ┌❖ **Perintah:** `{cmd}puasa5`\
        \n └❖ **Berfungsi : **Cie Ga puasa.\
        \n\n ┌❖ **Perintah:** `{cmd}puasa6`\
        \n └❖ **Berfungsi : **Bangga lu ga puasa?.\
        \n\n ┌❖ **Perintah:** `{cmd}takjil`\
        \n └❖ **Berfungsi : **Info Takjil Gratis.\
        \n\n ┌❖ **Perintah:** `{cmd}takjil2`\
        \n └❖ **Berfungsi : **ngajak nyari takjil.\
        \n\n ┌❖ **Perintah:** `{cmd}takjil3`\
        \n └❖ **Berfungsi : **gopudin cok.\
        \n\n ┌❖ **Perintah:** `{cmd}ngaji`\
        \n └❖ **Berfungsi : **gausah war mending ngaji.\
        \n\n ┌❖ **Perintah:** `{cmd}ngaji2`\
        \n └❖ **Berfungsi : **gapengen gibah.\
        \n\n ┌❖ **Perintah:** `{cmd}sabar`\
        \n └❖ **Berfungsi : **sabar lu kan lagi puasa.\
        \n\n ┌❖ **Perintah:** `{cmd}sabar2`\
        \n └❖ **Berfungsi : **cobain ajalah.\
        \n\n ┌❖ **Perintah:** `{cmd}setan1`\
        \n └❖ **Berfungsi : **ngatain orang setan.\
        \n\n ┌❖ **Perintah:** `{cmd}setan2`\
        \n └❖ **Berfungsi : **setan ngehasut setan.\
        \n\n ┌❖ **Perintah:** `{cmd}setan3`\
        \n └❖ **Berfungsi : **cie lagi ngehasut.\
        \n\n ┌❖ **Perintah:** `{cmd}sdkh`\
        \n └❖ **Berfungsi : **cobain aja males ngetik.\
        \n\n ┌❖ **Perintah:** `{cmd}sdkh2`\
        \n └❖ **Berfungsi : **sedekah baju lebaran.\
        \n\n ┌❖ **Perintah:** `{cmd}s1`\
        \n └❖ **Berfungsi : **sholat.\
        \n\n ┌❖ **Perintah:** `{cmd}s2`\
        \n └❖ **Berfungsi : **sholat.\
        \n\n ┌❖ **Perintah:** `{cmd}s3`\
        \n └❖ **Berfungsi : **sholat !.\
        \n\n ┌❖ **Perintah:** `{cmd}warteg`\
        \n └❖ **Berfungsi : **Info Warteg yang buka.\
        \n\n ┌❖ **Perintah:** `{cmd}warteg2`\
        \n └❖ **Berfungsi : **ngajak kewarteg.\
        \n\n ┌❖ **Perintah:** `{cmd}warteg3`\
        \n └❖ **Berfungsi : **Izin kewarteg.\
        \n\n ┌❖ **Perintah:** `{cmd}sahur`\
        \n └❖ **Berfungsi : **Ga disemangatin ayang sahurnya.\
        \n\n ┌❖ **Perintah:** `{cmd}sahur2`\
        \n └❖ **Berfungsi : **Sahur woi!!.\
        \n\n ┌❖ **Perintah:** `{cmd}buka`\
        \n └❖ **Berfungsi : **selamat berbuka.\
        \n\n ┌❖ **Perintah:** `{cmd}magrib`\
        \n └❖ **Berfungsi : **ciee nunggu adzan akunya kapan?.\
        \n\n ┌❖ **Perintah:** `{cmd}bukber`\
        \n └❖ **Berfungsi : **ngajak bukber gc.\
        \n\n ┌❖ **Perintah:** `{cmd}bukber2`\
        \n └❖ **Berfungsi : **Buat orang yg ngajak bukber tapi cuma wacana.\
        \n\n ┌❖ **Perintah:** `{cmd}bukber3`\
        \n └❖ **Berfungsi : **Bukber=Wacana.\
        \n\n ┌❖ **Perintah:** `{cmd}bukber4`\
        \n └❖ **Berfungsi : **Ngajar Bukber.\
        \n\n ┌❖ **Perintah:** `{cmd}bukbersad`\
        \n └❖ **Berfungsi : **cobain aja ya.\
        \n\n ┌❖ **Perintah:** `{cmd}taraw1`\
        \n └❖ **Berfungsi : **ngebilangin orang taraweh.\
        \n\n ┌❖ **Perintah:** `{cmd}taraw2`\
        \n └❖ **Berfungsi : **cobain aja ya.\
        \n\n ┌❖ **Perintah:** `{cmd}sholat`\
        \n └❖ **Berfungsi : **cobain aja ya."
    })
