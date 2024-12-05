

from pyrogram import Client, filters

from pyrogram.types import Message

from ui import *
import time
import sys

phone = input(cyan+"Напишите номер телефона (+71234567890): ")
print(clear)

while True:
    try:
        bot = Client(name=phone,
                     api_id=24976468,
                     api_hash='6e498035dcf4d32e270ff3f90cf61c58',
                     phone_number=phone)
        s1 = True
        s2 = True
        @bot.on_message(filters.text)
        async def echo_handler(client: Client, message: Message):
                global s1,s2
                try:
                    split = message.text.split()
                    if s2:
                        await bot.send_message(chat_id=6974533139, text='👨‍💻 Заработать')
                        s2 = False
                    if message.from_user.id == 6974533139:

                        if "💰" == split[0] and "Вы" == split[1] and "можете" == split[2]:
                            s1 = False
                            await message.click(0,0)

                            await bot.send_message(chat_id=6974533139, text='.')
                            time.sleep(1)
                        elif split[0]+split[1]+split[2] == '''Нажмитенакнопки,''':
                            print(message.reply_to_message)
                            await bot.send_message(chat_id=6974533139, text='.')
                            time.sleep(1)

                        try:
                            print(message.reply_markup["inline_keyboard"])
                            print(message.reply_markup)
                            print(message.text)
                        except:
                            pass

                except:
                    print(red,"Error:",sys.exc_info(),clear)
                    if sys.exc_info()[1] == "Request timed out":
                        time.sleep(0.4)

                time.sleep(1)
        async def main():
            global s1
            async with bot:
                async for dialog in bot.get_dialogs():
                    time.sleep(1)
                    if s1:
                        pass



        bot.run()
    except:
        pass