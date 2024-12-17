import requests

def shorten_url(long_url):
    try:
        # Используем API TinyURL для сокращения ссылки
        response = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}")
        
        # Проверяем статус ответа
        if response.status_code == 200:
            return response.text  # Возвращаем сокращенную ссылку
        else:
            print(f"Ошибка: не удалось получить ответ от TinyURL (статус: {response.status_code})")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при запросе: {e}")
        return None

if __name__ == "__main__":
    while True:
        long_url = input("Введите длинную ссылку для сокращения (или '0' для выхода): ")
        
        if long_url == '0':
            print("Выход из программы.")
            break

        shortened_url = shorten_url(long_url)
        if shortened_url:
            print(f"Сокращенная ссылка: {shortened_url}")
