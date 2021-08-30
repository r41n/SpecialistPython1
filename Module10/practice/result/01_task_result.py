# Напишите программу, вычисляющую площадь всех граней и объем прямоугольного параллелепипеда.
# Формат входных данных: даны три целые числа - ширина, высота и длина параллелепипеда.
# Формат выходных данных: вывести площадь всех граней и объем фигуры

# Важно!
# Оформите решение так, что работа с вашей программой была удобна пользователю.
# Пользователь должен понимать, что его просят ввести и что именно делает программа.

width = int(input("Введите ширину фигуры: "))
height = int(input("Введите высоту фигуры: "))
long = int(input("Введите длинну фигуры: "))

s = 2*((width * height) + (height + long) + (width + long))
v = width * height * long

print("Площадь -", s)
print("Объем -", v)
