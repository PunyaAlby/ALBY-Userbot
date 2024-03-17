FROM ayiinxd/ayiin-userbot:buster
RUN git clone -b ALBY-Userbot https://github.com/xfkm/nyoba /home/alby/ \
    && chmod 777 /home/alby \
    && mkdir /home/alby/bin/

COPY ./sample_config.env ./config.env* /home/alby/

WORKDIR /home/alby/

RUN pip install -r requirements.txt

CMD ["bash","start"]
