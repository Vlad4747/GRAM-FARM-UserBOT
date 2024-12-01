
from pyrogram import Client, filters

from pyrogram.types import Message

from ui import *

import time
import re

phone = input(cyan+"Напишите номер телефона (+71234567890): ")
print(clear)

while True:
    try:
        bot = Client(name=phone,
                     api_id=24976468,
                     api_hash='6e498035dcf4d32e270ff3f90cf61c58',
                     phone_number=phone)


        @bot.on_message(filters.text|filters.photo)
        async def echo_handler(client: Client, message: Message):
            if message.caption != None:
                if message.caption.startswith("https://t.me/piar_grambot?start=check_"):
                    check = str(message.caption).replace("https://t.me/piar_grambot?start=", "")
                    print(True, check)
                    await bot.send_message(6974533139, f"/start {check}")
            #print(message)
            if message.text.startswith("https://t.me/piar_grambot?start=check_"):
                check = message.text.replace("https://t.me/piar_grambot?start=","")
                print(True,check)

            time.sleep(0.1)
        bot.run()
    except:
        pass