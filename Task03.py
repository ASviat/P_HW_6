# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и LC.

my_list = [print(el, end=' ') for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]