# Церемония взвешивания
# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:

# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

# Формат входных данных
# На вход программе подаётся одно целое число.

# Формат выходных данных
# Программа должна вывести текст – название весовой категории.


# put your python code here
ves = int(input())
if ves < 60:
    print("Легкий вес")
if 60 <= ves < 64:
    print("Первый полусредний вес")
if 64 <= ves < 69:
    print("Полусредний вес")
