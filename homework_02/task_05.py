import random


def shuffle(ls):
    for i in range(len(ls)):
        pos = random.randint(0, len(ls) - 1)
        ls[i], ls[pos] = ls[pos], ls[i]
    return ls


ls = [i for i in range(20)]
print(ls)
print(shuffle(ls))
