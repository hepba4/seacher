def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Сдвигаем символы, игнорируя невидимые символы
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                encrypted_text += chr(start + (ord(char) - start + shift_amount) % 26)
            else:
                start = ord('A')
                encrypted_text += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    path = input("Введите путь к файлу: ")
    try:
        # Указание кодировки 'utf-8' при открытии файла
        with open(path, 'r', encoding='utf-8') as file:
            code = file.read()
        
        shift = 3  # Сдвиг для шифрования (можно поменять на другой)
        encrypted_code = encrypt(code, shift)

        output_filename = input("Введите имя для сохранения зашифрованного файла (без .py): ")
        output_filename += ".py"

        with open(output_filename, 'w', encoding='utf-8') as encrypted_file:
            encrypted_file.write(encrypted_code)

        print(f"Отлично, ваш код python зашифрован, и сохранен как: {output_filename}")

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь и попробуйте снова.")
    except UnicodeDecodeError:
        print("Ошибка декодирования. Проверьте кодировку вашего файла.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
