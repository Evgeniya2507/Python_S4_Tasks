# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа: n - кол-во элементов первого множества, 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


list_1 = set([int(i) for i in input('Введите целочисленные элементы первого списка: ').split()])
list_2 = set([int(i) for i in input('Введите целочисленные элементы второго списка: ').split()])
print(sorted(list(list_1.intersection(list_2))))