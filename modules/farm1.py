

from pyrogram import Client, filters

from pyrogram.types import Message

from ui import *
import time
import random

phone = input(cyan+"Напишите номер телефона (+71234567890): ")
print(clear)
s2 = True
def func():
    bot = Client(name=phone,
                 api_id=24976468,
                 api_hash='6e498035dcf4d32e270ff3f90cf61c58',
                 phone_number=phone)


    @bot.on_message(filters.text)
    async def echo_handler(client: Client, message: Message):
        global s2
        try:
            split = message.text.split()
            if s2:
                await bot.send_message(chat_id=6974533139, text='👨‍💻 Заработать')
                print(lgreen + "Отправлено: Заработать" + clear)
                s2 = False
            if message.from_user.id == 6974533139:

                if "💰" == split[0] and "Вы" == split[1] and "можете" == split[2]:
                    await message.click(0, 2)
                    time.sleep(0.01)
                    await bot.send_message(chat_id=6974533139, text='.')
                    print(lgreen + "Отправлено: ." + clear)
                    time.sleep(1)
                    print(lgreen+f"Нажатие на кнопку {clear}[0, 2]")
                elif "Чтобы" == split[0] and "получать" == split[1] and "грамм," == split[2]:
                    await message.click(0, 0)
                    print(lgreen+f"Нажатие на кнопку {clear}[0, 0]")
                elif "💰" == split[0] and "Вам" == split[1] and "начислено" == split[2]:
                    await message.click(0, 0)
                    print(lgreen+f"Нажатие на кнопку {clear}[0, 0]")
                elif "❌ Больше нет постов для просмотра." == message.text or "❌ Нету доступных заданий" == message.text:
                    print(cyan + "Задания на просмор постов закончились")
                    print("Проверка новых заданий будет через 3 минуту")
                    print(clear)
                    print(lgreen + "Перезапуск..." + clear)
                    return None
        except:
            print(red + "Ошибка при обработке сообщения" + clear)
        time.sleep(1)



    bot.run()

while True:
    try:
        print(lgreen+"Запуск..."+clear)
        func()
        time.sleep(180+random.random()*3)
        print(lgreen+bold + "3 минута прошла" + clear)
    except:
        pass