FROM punyaalby/alby-userbot:buster
#━━━━━ ALBY-Userbot ━━━━━━

RUN git clone -b ALBY-Userbot https://github.com/PunyaAlby/ALBY-Userbot /home/albyuserbot/ \
    && chmod 777 /home/albyuserbot \
    && mkdir /home/albyuserbot/bin/
WORKDIR /home/albyuserbot/

RUN pip3 install -r https://raw.githubusercontent.com/PunyaAlby/ALBY-Userbot/ALBY-Userbot/requirements.txt

CMD ["python3", "-m", "userbot"]
