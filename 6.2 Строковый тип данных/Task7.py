# Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

# Примечание. Гарантируется, что длины названий всех трех городов различны.

# put your python code here
city1 = str(input())
city2 = str(input())
city3 = str(input())
length1 = len(city1)
length2 = len(city2)
length3 = len(city3)
if length2 > length1 < length3:
    print(city1)
elif length1 > length2 < length3:
    print(city2)
else:
    print(city3)
if length2 < length1 > length3:
    print(city1)
elif length1 < length2 > length3:
    print(city2)
else:
    print(city3)
