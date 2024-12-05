


import time
from ui import *
import os

os.system("clear")




print(bannerBig)




while True:
    try:
        print(menu)
        command = input("Введите команду: ")
        print(purple+"Список сессий:")
        for file in os.listdir():
            if file.endswith(".session"):
                print("|")
                print(os.path.join("-->  "+file[:-8]))
        print(clear)
        match command:
            case "1":
                import modules.farm1
            case "2":
                import modules.farm2
            case "3":
                name = input("Введите название сессии: ")
                os.remove(f"{name}.session")
    except:
        pass