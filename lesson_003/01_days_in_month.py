# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)


more_days = (1, 3, 5, 7, 8, 10, 12)
less_days = (4, 6, 9, 11)
february = 2

if month in more_days:
    print("31")
elif month in less_days:
    print("30")
elif month == february:
    print("28")
else:
    print("Номер месяца некорректен")

#TODO с февралём лучше сделать так или
# elif month == 2