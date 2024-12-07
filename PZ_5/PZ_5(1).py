#Найти сумму чисел ряда 1, 2, 3, 4,... от числа n до m. Суммирование оформить функцией с параметрами.Значения n и m программа должна запрашивать
def sum_numbers(n,m):
    sum=0
    for i in range(n,m+1):sum += i
    return sum
while True:
    try:
       n = int(input("Введите первое число:"))
       break
    except ValueError:
        print("Неправильно ввели!")
while True:
    try:
      m = int(input("Введите второе число "))
      break
    except ValueError:
        print("Неправильно ввели!")
result = sum_numbers(n,m)
print(f"Сумма чисел от {n} до {m} равна {result}")