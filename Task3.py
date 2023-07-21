#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input())
# i = 2
# nn = 1
# while i <= n:
#     i *= 2
#     nn += 1
# print(nn - 1, i // 2)

n = int(input('Введите число N '))
degree = 1
i = 1
while degree <= n:
    degree *= 2
    i += 1
    print(i - 1, degree // 2)