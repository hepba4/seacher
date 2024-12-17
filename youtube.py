from pytube import YouTube

def download_video(video_url):
    try:
        # Создаем объект YouTube
        yt = YouTube(video_url)

        # Выводим информацию о видео
        print(f"Название: {yt.title}")
        print(f"Длительность: {yt.length} секунд")
        
        # Выбираем стрим для скачивания (обычно выбираем поток с наилучшим качеством видео)
        stream = yt.streams.get_highest_resolution()

        # Скачиваем видео
        print("Начинаем скачивание...")
        stream.download()  # Скачивание в текущую директорию
        print("Скачивание завершено!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    while True:
        # Ссылка на видео YouTube для скачивания
        video_url = input("Введите URL видео YouTube (или '0' для выхода): ")
        
        if video_url == '0':
            print("Выход из программы.")
            break
        
        download_video(video_url)
