# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x and y and z) == (not x) or (not y) or (not z):
                print('Верно для x = {}, y = {}, z = {}'.format(x, y, z))
            else:
                print('Не верно для x = {}, y = {}, z = {}'.format(x, y, z))
