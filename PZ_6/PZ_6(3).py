#Дан список A размера N и целое число K (! < K < 4,K < N).Осуществить циклический сдвиг элементов спискавправо на K позиций(при этом А1 перейдет в Ak+1, A2-в Ak+2, ..., An-в Ak).Допускается использовать вспомогательный список из 4 элементов.
def cyclic_shift_right(A, K):
    N = len(A)
    temp = [0] * 4
    for i in range(K):
        temp[i] = A[N - K + i]
    for i in range(N - 1, K - 1, -1):
        A[i] = A[i - K]
    for i in range(K):
        A[i] = temp[i]
def main():
    try:
        N = int(input("Введите размер списка N (N > 4): "))
        if N <= 4:
            raise ValueError("Размер списка N должен быть больше 4.")
        K = int(input("Введите целое число K (1 < K < 4 и K < N): "))
        if not (1 < K < 4 and K < N):
            raise ValueError("K должно быть больше 1 и меньше 4, а также меньше N.")
        A = []
        print(f"Введите {N} элементов списка:")
        for _ in range(N):
            element = int(input())
            A.append(element)
        print("Исходный список:", A)
        cyclic_shift_right(A, K)
        print("Список после циклического сдвига вправо на K позиций:", A)
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите корректные данные.")