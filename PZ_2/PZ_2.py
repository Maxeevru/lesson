#Дано трехзначное число. Найти сумму и произведение его цифр.
try:
    number = int(input("Введите трехзначное число: "))
    if number < 100 or number > 999:
        raise ValueError("Число должно быть трехзначным")
    s = (number // 100) + ((number % 100) // 10) + (number % 10)
    p = (number // 100) * ((number % 100) // 10) * (number % 10)
    print(f"Сумма цифр числа {number}: {s}")
    print(f"Произведение цифр числа {number}: {p}")
except ValueError as e:
    print(f"Ошибка: {e}. Пожалуйста, введите корректное целое число.")