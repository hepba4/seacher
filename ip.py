from colorama import Fore, init
init()
import time
import urllib.request
import json
import os

getIP = input(Fore.RED + "Введите IP: ")
url = "https://ipinfo.io/" + getIP + "/json"
try:
    getInfo = urllib.request.urlopen(url)
except:
    print(Fore.RED + 'IP не найдено')
infoList = json.load(getInfo)
def whoisIPinfo(ip):
    try:
        myComand = "whois " + getIP
        whoisInfo = os.popen(myComand).read()
        return whoisInfo
    except:
        return "Ошибка"

print(Fore.RED + "IP: ", infoList["ip"])
print(Fore.RED + "Город: ", infoList["city"])
print(Fore.RED + "Регион: ", infoList["region"])
print(Fore.RED + "Страна: ", infoList["country"])
print(Fore.RED + "Временная зона: ", infoList["timezone"])
print(Fore.RED + "Координаты: ", infoList["loc"])
print(Fore.RED + "Название хоста: ", infoList["hostname"])
print(Fore.RED + "Индекс: ", infoList["postal"])
exit = input(Fore.RED + "Чтобы выйти нажмите enter....")