import random


def guess_the_number():
    print("Игра «Угадай число»")
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            user_guess = int(input("Твой вариант: "))
            attempts += 1

            if user_guess < secret_number:
                print("Загаданное число больше.")
            elif user_guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number}!")
                print(f"Количество попыток: {attempts}")
                break
        except ValueError:
            print("Пожалуйста, введи целое число.")


if __name__ == "__main__":
    guess_the_number()
