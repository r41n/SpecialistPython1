# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: для генерации случайного числа используйте import random

import random


def gen_random_list(size, min_value=-20, max_value=20):
    list_el = []
    for _ in range(size):
        list_el.append(random.randint(min_value, max_value))
    return list_el


print(gen_random_list(25))
