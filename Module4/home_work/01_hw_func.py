# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    number = str(ticket_number)
    summa1 = int(number[:1]) + int(number[1:2])
    summa2 = int(number[-1]) + int(number[-2])
    if summa1 == summa2:
        return True
    return False



# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
