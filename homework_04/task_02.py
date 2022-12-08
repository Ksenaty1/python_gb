# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def razl(x):
    ls = [1]
    d = 2
    while d ** 2 <= x:
        if x % d == 0:
            ls.append(d)
            x //= d
        else:
            d += 1
    if x > 1:
        ls.append(x)
    return list(set(ls))



n = 6
print(razl(n))