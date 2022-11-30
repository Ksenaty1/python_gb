import random

n = int(input(">>> Введите N:"))
subseq = [random.randint(-n, n) for i in range(n)]
pos = []
with open("file.txt") as file:
    for line in file:
        pos.append(int(line))

answer = 1
for posit in pos:
    answer *= subseq[posit]

print(subseq)
print(answer)