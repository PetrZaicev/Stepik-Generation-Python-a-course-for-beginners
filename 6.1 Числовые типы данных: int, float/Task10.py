# Сортировка трёх 🌶️
# Напишите программу, которая упорядочивает три числа от большего к меньшему.

# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.


a, b, c = int(input()), int(input()), int(input())
maximum = max(a, b, c)
minimum = min(a, b, c)
if a == maximum:
    print(a)
if b == maximum:
    print(b)
if c == maximum:
    print(c)
if a != maximum and a != minimum:
    print(a)
if b != maximum and b != minimum:
    print(b)
if c != maximum and c != minimum:
    print(c)
if a == minimum:
    print(a)
if b == minimum:
    print(b)
if c == minimum:
    print(c)
