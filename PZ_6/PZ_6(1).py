#Дан список A размера N. Вынести его элементы в следующем  порядке: A1, A2, An,An-1,A3,A4,An-2,An-3,... .
def rearrange_list(A):
    if not isinstance(A, list):
        raise ValueError("Входные данные должны быть списком.")
    if len(A) == 0:
        raise ValueError("Список не должен быть пустым.")    
    N = len(A)
    result = []
    left = 0
    right = N - 1
    while left <= right:
        if left < N:
            result.append(A[left])
            left += 1
        if right >= 0 and right != left - 1:
            result.append(A[right])
            right -= 1
    return result
try:
    A = [1, 2, 3, 4, 5]
    rearranged = rearrange_list(A)
    print(rearranged)
except ValueError as e:
    print(f"Ошибка: {e}")