


import time
from ui import *
import os

os.system("clear")

print(bannerBig)




while True:
    try:
        print(menu)
        command = input("Введите команду: ")
        match command:
            case "1":
                import modules.farm1
            case "2":
                import modules.farm2
            case "3":
                import modules.farm3
    except:
        pass