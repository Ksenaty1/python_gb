# Вычислить число Пи c заданной точностью d


import math


def accuracy(d):
    x = 0
    while d != 1.0:
        d *= 10
        x += 1
    return x

d = 0.001
print(str(math.pi)[:accuracy(d) + 2])