def generate_squares_dict(n):
    return {i: i**2 for i in range(1, n + 1)}


if __name__ == "__main__":
    print("Генератор словаря квадратов чисел")

    while True:
        try:
            n = int(input("Введите целое число N: "))

            if n < 1:
                print("Ошибка: введите число больше нуля. Попробуйте снова.")
            else:
                squares_dict = generate_squares_dict(n)
                print(f"Словарь квадратов от 1 до {n}:")
                print(squares_dict)
                break

        except ValueError:
            print("Ошибка: вы ввели не целое число. Попробуйте снова.")
