from pystyle import Write, Colors
from phonenumbers import parse, is_valid_number, is_possible_number, carrier, geocoder, timezone, PhoneNumberFormat, format_number

def phoneinfo(phone):
    try:
        # Парсинг номера телефона
        parsed_phone = parse(phone, None)
        
        # Проверка валидности номера
        if not is_valid_number(parsed_phone):
            Write.Print("\n[!] Произошла ошибка -> Недействительный номер телефона\n", Colors.red_to_yellow, interval=0.005)
            return
        
        # Получение информации о номере
        carrier_info = carrier.name_for_number(parsed_phone, "en")
        country = geocoder.description_for_number(parsed_phone, "en")
        region = geocoder.description_for_number(parsed_phone, "ru")
        formatted_number = format_number(parsed_phone, PhoneNumberFormat.INTERNATIONAL)
        is_valid = is_valid_number(parsed_phone)
        is_possible = is_possible_number(parsed_phone)
        
        # Форматирование и вывод информации
        print_phone_info = f"""
[+] Номер телефона -> {formatted_number}
[+] Страна -> {country}
[+] Регион -> {region}
[+] Оператор -> {carrier_info}
[+] Активен -> {is_possible}
[+] Валид -> {is_valid}
[+] Telegram -> https://t.me/{phone}
[+] Whatsapp -> https://wa.me/{phone}
[+] Viber -> https://viber.click/{phone}\n"""
        
        Write.Print(print_phone_info, Colors.red_to_yellow, interval=0.005)
    except Exception as e:
        Write.Print(f"\n[!] Произошла ошибка -> {str(e)}\n", Colors.red_to_yellow, interval=0.005)

def main():
    # Ввод номера телефона
    phone = Write.Input("\n[?] Введите номер телефона -> ", Colors.red_to_yellow, interval=0.005)
    phoneinfo(phone)

if __name__ == "__main__":
    main()