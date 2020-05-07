# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись отображает сколько и по какой цене закупалось товаров.
#
# Задание: вывести суммарную стоимость каждого ВИДА товара на складе c помощью циклов
#
# Формат вывода:
#   <товар_1> - <кол-во_товара_1> шт, стоимость <общая_стоимость_товара_1> руб
#   <товар_2> - <кол-во_товара_2> шт, стоимость <общая_стоимость_товара_2> руб
#   <товар_4> - <кол-во_товара_3> шт, стоимость <общая_стоимость_товара_3> руб
#
# Например:
#   Стул - 1111 шт, стоимость 8888 руб
#   Диван - 2222 шт, стоимость 9999 руб
#   и так далее
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

for item in goods.items():
    print(item)
lamp_cost = 0
lamp_quantity = 0
table_cost = 0
table_quantity = 0
sofa_cost = 0
sofa_quantity = 0
chair_cost = 0
chair_quantity = 0

for key, val in store.items():
    if key == "12345":
        lamp_quantity = val[0].get("quantity")
        lamp_cost = val[0].get("quantity") * val[0].get("price")
        print("Лампа -", lamp_quantity, "шт, стоимость", lamp_cost, "руб")
        continue
    if key == "23456":
        table_quantity = val[0].get("quantity") + val[1].get("quantity")
        table_cost = val[0].get("quantity") * val[0].get("price") + val[1].get("quantity") * val[1].get("price")
        print("Стол -", table_quantity, "шт, стоимость", table_cost, "руб")
        continue
    if key == "34567":
        sofa_quantity = val[0].get("quantity") + val[1].get("quantity")
        sofa_cost = val[0].get("quantity") * val[0].get("price") + val[1].get("quantity") * val[1].get("price")
        print("Диван -", sofa_quantity, "шт, стоимость", sofa_cost, "руб")
        continue
    if key == "45678":
        chair_quantity = val[0].get("quantity") + val[1].get("quantity") + val[2].get("quantity")
        chair_cost = val[0].get("quantity") * val[0].get("price") + val[1].get("quantity") * val[1].get("price") + val[
            2].get("quantity") * val[2].get("price")
        print("Стул -", chair_quantity, "шт, стоимость", chair_cost, "руб")






