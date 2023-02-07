# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

script_name, time_spent, money_per_hour, my_bonus = argv

my_ammount = int(time_spent)*int(money_per_hour)+int(my_bonus)

print(f'Сумма к выплате: {my_ammount}')

# python Task01.py 10 25 500
