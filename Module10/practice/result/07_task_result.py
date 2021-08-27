# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.

import random

num = random.randint(20000, 29999)
numbers = str(num)

with open("random_int.txt", "w") as f:
    f.writelines(numbers)
