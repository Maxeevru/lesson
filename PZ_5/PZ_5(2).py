#Описать функцию Power1(A,B) вещественного типа,находящего величину AB по формуле AB=exp(B*(lnA))(параметры A и B вещественные).В случае нулевого или отрицательного парамера A функция возвращает 0.Найти степени A*P,B*P,C*P,если даны числа P, A, B, C.
import math
def Power1(A, B):
    if A <= 0:
        return 0
    else:
        return math.exp(B * math.log(A))
while True:
    try:
        P = int(input("Введите число P: "))
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        C = int(input("Введите число C: "))
        
        result_A = pow(A, P)
        result_B = pow(B, P)
        result_C = pow(C, P)

        print(f"A в степени P: {result_A}")
        print(f"B в степени P: {result_B}")
        print(f"C в степени P: {result_C}")

        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите целые числа.")