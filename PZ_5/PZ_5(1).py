def sum_numbers(n,m):
    sum=0
    for i in range(n,m+1):sum += i
    return sum
n = int(input("Введите первое число:"))
m = int(input("Введите второе число "))
result = sum_numbers(n,m)
print(f"Сумма чисел от {n} до {m} равна {result}")