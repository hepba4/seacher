import os
import subprocess

# Файл для хранения общего числа сгенерированных ключей
count_file = "total_ssh_keys_generated.txt"

def read_total_count():
    """Читает общее количество сгенерированных ключей из файла."""
    if os.path.exists(count_file):
        with open(count_file, 'r') as file:
            return int(file.read().strip())
    return 0

def write_total_count(count):
    """Записывает общее количество сгенерированных ключей в файл."""
    with open(count_file, 'w') as file:
        file.write(str(count))

def generate_ssh_key(key_number):
    """Генерирует SSH-ключи и сохраняет их в файле с уникальным именем."""
    key_name = f"id_rsa_{key_number}"  # Название ключа
    key_path = os.path.join(os.getcwd(), key_name)  # Путь к файлу ключа

    # Команда для генерации SSH-ключа
    command = ["ssh-keygen", "-t", "rsa", "-b", "2048", "-f", key_path, "-N", ""]

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"SSH-ключи сгенерированы: {key_name}.pub (открытый) и {key_name} (закрытый)")
        return True
    except subprocess.CalledProcessError:
        print(f"Ошибка при генерации SSH-ключа {key_number}. Попробуйте снова.")
        return False

def main():
    total_count = read_total_count()  # Чтение общего количества ключей из файла

    while True:
        try:
            count = int(input("Сколько SSH-ключей сгенерировать? (введите число, 0 для выхода) "))
            if count == 0:
                print("Выход из программы.")
                break
            elif count < 0:
                print("Пожалуйста, введите положительное число или 0 для выхода.")
                continue
            
            for i in range(1, count + 1):
                if generate_ssh_key(total_count + i):
                    total_count += 1  # Увеличиваем общее количество сгенерированных ключей

            write_total_count(total_count)  # Записываем новое общее количество в файл
            print(f"\nСгенерировано всего {total_count} SSH-ключей.")
        
        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    main()
