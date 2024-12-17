from faker import Faker
from colorama import Fore , Style
import os
import pyfiglet

fak = Faker()
ru = Faker('ru_RU')

while True:
    p = pyfiglet.figlet_format('    DeepFake', font='ogre')
    print(Fore.BLUE + p + Style.RESET_ALL)
    print(Fore.RED + 'выход ctrl + C' + Style.RESET_ALL)
    print('')
    f = input(Fore.BLUE + "...ENTER..." + Style.RESET_ALL)
    print(Fore.BLUE + '_____ФИО_____' + Style.RESET_ALL)
    print(Fore.BLUE + ru.name() + Style.RESET_ALL)
    print(Fore.BLUE + '_____Ник нейм_____' + Style.RESET_ALL)
    print(Fore.BLUE + ru.user_name() + Style.RESET_ALL)
    print(Fore.BLUE + '_____Адреса_____' + Style.RESET_ALL)
    print(Fore.BLUE + 'Идекс:' , ru.postcode() + Style.RESET_ALL)
    print(Fore.BLUE + 'Название улицы:' , ru.street_name())
    print(Fore.BLUE + 'Адрес на улице:' , ru.street_address())
    print(Fore.BLUE + 'Название страны:', ru.country())
    print(Fore.BLUE + 'Название города:' , ru.city())
    print(Fore.BLUE + 'Полный адрес:' , ru.address())
    print(Fore.BLUE + '_____Професия_____' + Style.RESET_ALL)
    print(Fore.BLUE + ru.job() + Style.RESET_ALL)
    print(Fore.BLUE + '_____Кредитная карта_____' + Style.RESET_ALL)
    print(Fore.BLUE + ru.credit_card_number() + Style.RESET_ALL)
    print(Fore.BLUE + '_____Номер телефона_____' + Style.RESET_ALL)
    print(Fore.BLUE + 'Номер телефона' , ru.phone_number() + Style.RESET_ALL)
    print(Fore.BLUE + '_____Почта_____'  + Style.RESET_ALL)
    print(Fore.BLUE + ru.email() + Style.RESET_ALL)
    print(Fore.BLUE + '_____Компания_____' + Style.RESET_ALL)
    print(Fore.BLUE + ru.company() + Style.RESET_ALL)
    print(Fore.BLUE + '_____Рандомный текст_____' + Style.RESET_ALL)
    print(Fore.BLUE + ru.text() + Style.RESET_ALL)
    f = input(Fore.BLUE + "...ENTER..." + Style.RESET_ALL)
    os.system('clear')
