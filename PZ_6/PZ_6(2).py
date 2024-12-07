#Дан целочисленный список размера N,содержащий ровно два одинаковых элемента.Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.
def find_duplicate_indices(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list.")    
    if len(arr) < 2:
        raise ValueError("List must contain at least two elements.")    
    index_map = {}   
    for index, value in enumerate(arr):
        if value in index_map:
            return sorted([index_map[value], index])
        index_map[value] = index    
    raise ValueError("No duplicate elements found in the list.")
try:
    arr = [1, 2, 3, 4, 2]
    indices = find_duplicate_indices(arr)
    print("Индексы одинаковых элементов:", indices)
except ValueError as e:
    print("Ошибка:", e)