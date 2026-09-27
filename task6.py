def calculator():
    print("Консольный калькулятор")

    while True:
        try:
            a = float(input("Введите первое число: "))
            operator = input("Выберите операцию (+, -, *, /): ")
            b = float(input("Введите второе число: "))

            if operator == '+':
                result = a + b
            elif operator == '-':
                result = a - b
            elif operator == '*':
                result = a * b
            elif operator == '/':
                if b == 0:
                    print("Ошибка: деление на ноль невозможно! Попробуйте "
                          "снова.\n")
                    continue
                result = a / b
            else:
                print("Ошибка: неизвестная операция! Попробуйте снова.\n")
                continue

            print(f"Результат: {a} {operator} {b} = {result}")
            break

        except ValueError:
            print("Ошибка: введено некорректное число! Попробуйте снова.\n")


if __name__ == "__main__":
    calculator()
