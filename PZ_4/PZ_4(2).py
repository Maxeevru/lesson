#Даны положительные числа A и B(А > Б).На отрезке длины A размещено возможное количество отрезков длины В(без наложений.Не используя операции умножения и деления,найти колво отрезков
def count_segments(A, B):
    count = 0
    remaining_length = A
    while remaining_length >= B:
        count += 1
        remaining_length -= B
    return count
def main():
    try:
        A = float(input("Введите положительное число A (A > B): "))
        B = float(input("Введите положительное число B: "))
        if A <= 0 or B <= 0:
            raise ValueError("A и B должны быть положительными числами.")
        if A <= B:
            raise ValueError("A должно быть больше B.")
        result = count_segments(A, B)
        print(f"Количество отрезков длины B, которые можно разместить на отрезке длины A: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректные данные.")