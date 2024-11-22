number = int(input("Введите трехзначное число"))
if not 100 <= number <= 999:
    raise ValueError("Число должно быть трехзначным")
s = (number // 100) + ((number % 100) // 10) + (number % 10)
p = (number // 100) * ((number % 100) // 10) * (number % 10)
print(f"Сумма цифр числа {number}: {s}")
print(f"Произведение цифр числа {number}: {p}")