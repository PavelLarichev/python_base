# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1100, 500)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
x_list = []
y_list = []
length_list = []

for _ in range(N):
    x_num = sd.random_number(100, 900)
    y_num = sd.random_number(550, 650)
    length_num = sd.random_number(10, 100)
    x_list.append(x_num)
    y_list.append(y_num)
    length_list.append(length_num)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


while True:
    sd.start_drawing()
    for i in range(N):
        point = sd.get_point(x_list[i], y_list[i])
        length = length_list[i]
        sd.snowflake(center=point, length=length, color=sd.background_color)
        y_list[i] -= 65
        if y_list[i] <= 50:
            break
        point1 = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point1, length=length, color=sd.COLOR_WHITE)
        sd.sleep(0.01)
    sd.finish_drawing()
    if sd.user_want_exit():
        break
sd.pause()

# Зачет!