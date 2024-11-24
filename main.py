
from pyrogram import Client, filters

from pyrogram.types import Message

import time
while True:
    try:
        yellow = '\033[93m'
        lgreen = '\033[92m'
        clear = '\033[0m'
        bold = '\033[01m'
        cyan = '\033[96m'
        red = "\033[91m"

        print(lgreen+f'''
    GRAM FARM UserBOT {yellow}V0.0.1{clear}
        Создатель {cyan}тг:{bold}@LORDSYSTEMM
        ''')

        phone = input(cyan+"Напишите номер телефона (+71234567890): ")
        print(clear)

        # now if you use logger it will not log to console.

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
                            print(message.id)
                            s1 = False
                            await message.click(0,2)
                            await bot.send_message(chat_id=6974533139, text='.')
                        elif "Чтобы" == split[0] and "получать" == split[1] and "грамм," == split[2]:
                            await message.click(0, 0)
                        elif "💰" == split[0] and "Вам" == split[1] and "начислено" == split[2]:
                            await message.click(0, 0)
                        elif "❌ Больше нет постов для просмотра." == message.text or "❌ Нету доступных заданий" == message.text:
                            time.sleep(60)
                            await bot.send_message(chat_id=6974533139, text='👨‍💻 Заработать')
                except:
                    print(red+"Ошибка при получении сообщения"+clear)
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