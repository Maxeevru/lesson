#Дан список A размера N и целое число K (! < K < 4,K < N).Осуществить циклический сдвиг элементов спискавправо на K позиций(при этом А1 перейдет в Ak+1, A2-в Ak+2, ..., An-в Ak).Допускается использовать вспомогательный список из 4 элементов. 
def calculate_expression(A, N):
    result = 0.0
    current_term = 1.0
    for i in range(N + 1):
        result += current_term * ((-1) ** i)
        current_term *= A
    return result
def main():
    try:
        A = float(input("Введите вещественное число A: "))
        N = int(input("Введите целое число N (>0): "))
        if N <= 0:
            raise ValueError("N должно быть больше 0.")
        result = calculate_expression(A, N)        
        print(f"Значение выражения 1 - A + A^2 - A^3 + ... + (-1)^N * A^N: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректные данные.")