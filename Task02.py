# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
# Реализуйте с list comprehension

num = int(input('Из скольки элементов хотите список? '))

my_list = [int(input(f'Введите элемент {el+1}: ')) for el in range(0, num)]

print(my_list)

my_list_sec = [my_list[el] for el in range(len(my_list)) if my_list[el-1] < my_list[el]]

print(my_list_sec)