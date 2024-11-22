A = int(input("Введите целое число A"))
B =int(input("Введите целое число B"))
C =int(input("Введите целое число C"))
countpositive = 0
if A > 0:
    countpositive += 1
if B > 0:
    countpositive += 1
if C > 0:
    countpositive += 1
if countpositive == 2:
    print("Истинно: Два из чисел A, B, C являются положительными")
else:
    print("Ложно: Не два числа из A, B, C являются положительными или больше двух")