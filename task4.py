def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print("Программа для вычисления НОД для двух чисел")

    while True:
        try:
            num1 = int(input("Введите первое целое число: "))
            num2 = int(input("Введите второе целое число: "))

            gcd = find_gcd(abs(num1), abs(num2))
            print(f"Наибольший общий делитель чисел {num1} и {num2} "
                  f"равен: {gcd}")

            break

        except ValueError:
            print("Ошибка: вводите только целые числа. Попробуйте снова.\n")
