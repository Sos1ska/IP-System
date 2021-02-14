import os
import time
import urllib.request
import json

Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
Underline = '\033[4m'
end       = '\033[0m'

print(f"{Red}{Underline}Sos-BreakIP 1.0{end}")
os.system("toiet -f big ' Sos1ska-Hackers' -F gat | lolcat")

print(f"{Yellow}Добро пожаловать в мой первый пробив IP-адреса{end}")
time.sleep(2)
os.system("clear")

while True:
    print(f"{Red}{Underline}Sos-BreakIP 1.0{end}")
    print(f"Для продолжения введите {Green}y{end}/{Red}n{end}")
    start_input = input(Green + "Введите ответ " + end)
    if str(start_input) == "y":
        os.system("clear")
        print(f"{Yellow}\t\t\tЗапускаю утилиту: {end} /")
        time.sleep(1)
        os.system("clear")
        print(f"{Yellow}\t\t\tЗапускаю утилиту: {end} \ ")
        time.sleep(1)
        os.system("clear")
        print(f"{Yellow}\t\t\tЗапускаю утилиту: {end} | ")
        time.sleep(1)
    if str(start_input) == "n":
        print(f"\t\t\t{Yellow}Выключаюсь{end}")
        time.sleep(1)
        os.system("clear")
        print(f"\t\t\t{Yellow}Утилита выключена{end}")
        quit()
    print(f"{Yellow}Введите IP-адрес{end}")
    ip_input = input(Green + ">>> " + end)

    getInfo = (f"https://htmlweb.ru/geo/api.php?json&ip={str(ip_input)}")
    try:
        infoIP = urllib.request.urlopen( getInfo)
    except:
        print(f"\n[!] - {Red}IP-адрес введён не верно{end} - [!]")
    
    infoIP = json.load( infoIP )

    try:
        print(f"{Yellow}Страна: {end}", infoIP["country"]["fullname"])
    except KeyError:
        print(f"{Yellow}Страна: Не удалось определить{end}")
    try:
        print(f"{Yellow}Столица: {end}", infoIP["id"]["name"])
    except KeyError:
        print(f"{Yellow}Столица: Не удалось определить{end}")
    try:
        print(f"{Yellow}Широта столицы: {end}", infoIP["id"]["latitude"])
    except KeyError:
        print(f"{Yellow}Широта столицы: Не удалось определить{end}")
    try:
        print(f"{Yellow}Долгота столицы: {end}", infoIP["id"]["longitude"])
    except KeyError:
        print(f"{Yellow}Долгота столицы: Не удалось определить")
    try:
        print(f"{Yellow}Коды номеров телефонов столицы: ", infoIP["id"]["telcod"])
    except KeyError:
        print(f"{Yellow}Коды номеров телефоно столицы: Не удалось определить{end}")
    try:
        print(f"{Yellow}Город: ", infoIP["country"]["city"])
    except KeyError:
        print(f"{Yellow}Город: Не удалось определить{end}")
    try:
        print(f"{Yellow}Широта города: ", infoIP["country"]["latitude"])
    except KeyError:
        print(f"{Yellow}Широта города: Не удалось определить{end}")
    try:
        print(f"{Yellow}Долгота города: ", infoIP["country"]["longitude"])
    except KeyError:
        print(f"{Yellow}Долгота города: Не удалось определить{end}")
    try:
        print(f"{Yellow}Код автомобилей города: ", infoIP["region"]["autocod"])
    except KeyError:
        print(f"{Yellow}Код автомобилей города: Не удалось определить{end}")
    try:
        print(f"{Yellow}Область: ", infoIP["region"]["name"])
    except KeyError:
        print(f"{Yellow}Область: Не удалось определить{end}")
    try:
        print(f"{Yellow}Округ: ", infoIP["region"]["okrug"])
    except KeyError:
        print(f"{Yellow}Округ: Не удалось оперделить{end}")
    try:
        print(f"{Yellow}Язык: ", infoIP["region"]["country"])
    except KeyError:
        print(f"{Yellow}Язык: Не удалось определить")
    except KeyboardInterrupt:
        sys.exit(f"\t\t\t{Red}Вынужденная остановка кода")


    print(f"{Yellow}Выйти или продолжить? Для продолжение введите клавишу Enter, для выхода 0{end}")
    exit_input = input(Green + ">>> " + end)
    if str(exit_input) == "0":
        os.system("clear")
        print(f"{Yellow}В ВК можете оценить данный скрипт, вот профиль {end}{Green}>>> {end}{Blue}https://vk.com/nikitasos1ska")
        quit()