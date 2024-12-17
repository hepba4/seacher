import openai

def main():
    # Запрос токена API
    api_token = input("Введите токен OpenAI API: ")
    openai.api_key = api_token

    print("Чат с GPT. Введите 'выход' для завершения.")

    while True:
        # Ввод сообщения от пользователя
        user_input = input("Вы: ")
        
        if user_input.lower() == 'выход':
            print("Завершение чата.")
            break

        try:
            # Генерация ответа от GPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Вы можете изменить модель на актуальную
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )

            # Вывод ответа
            gpt_response = response['choices'][0]['message']['content']
            print(f"GPT: {gpt_response}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
