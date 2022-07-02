#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b ALBY-Userbot https://github.com/PunyaAlby/Userbot /home/albyuserbot/ \
    && chmod 777 /home/albyuserbot \
    && mkdir /home/albyuserbot/bin/

COPY ./sample_config.env ./config.env* /home/albyuserbot/

WORKDIR /home/albyuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
