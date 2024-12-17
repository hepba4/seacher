import requests
from colored import fore, back, style

def check_url_safety():
    link = input("Введите URL для проверки безопасности: ")
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print(f"{link} безопасная ссылка.")
        else:
            print(f"{link} потенциально опасная ссылка.")
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при проверке {link}: {str(e)}")

check_url_safety()