def recursive_sum(n):
    # Базовый случай: если n = 1, сумма равна 1
    if n == 1:
        return 1
    # Рекурсивный случай
    return n + recursive_sum(n - 1)


if __name__ == "__main__":
    print("Рекурсивная сумма чисел от 1 до N")

    while True:
        try:
            user_input = int(input("Введите целое число (больше 0): "))

            if user_input < 1:
                print("Ошибка: число должно быть >=1. Попробуйте снова.")
            else:
                result = recursive_sum(user_input)
                print(f"Сумма чисел от 1 до {user_input} равна: {result}")
                break

        except ValueError:
            print("Ошибка: вы ввели не целое число. Попробуйте снова.")

        except RecursionError:
            print("Ошибка: слишком большое число! Ппереполнение стека.")
            print("Пожалуйста, введите число поменьше (например, до 999).")
