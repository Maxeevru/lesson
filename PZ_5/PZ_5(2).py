P = int(input("Введите число P"))
A = int(input("Введите число A"))
B = int(input("Введите число B"))
C = int(input("Введите число C"))
import math
def Power1(A, B):
    if A <= 0:
        return 0
    else:
        return math.exp(B * math.log(A))
result_A =pow(A,P)
result_B = pow(B,P)
result_C = pow(C,P)
print(f"A в степени P: {result_A}")
print(f"B в степени P: {result_B}")
print(f"C в степени P: {result_C}")