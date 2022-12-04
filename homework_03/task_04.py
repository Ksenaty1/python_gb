# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from random import randint

# Задаем число и заранее узнаем ответ с помощью встроенной функции bin()
number = randint(0, 100)
print(number)
print(bin(number)[2:])

# Находим ответ
bin_num = ''
while number > 0:
    bin_num = str(number % 2) + bin_num
    number //= 2

print(bin_num)
