# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


import random


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile():
    x = random.randint(0, 600)
    sd.circle(center_position=sd.get_point(x + 100, x + 100), radius=50)
    sd.circle(center_position=sd.get_point(x + 80, x + 120), radius=10)
    sd.circle(center_position=sd.get_point(x + 125, x + 120), radius=10)
    sd.line(start_point=sd.get_point(x + 80, x + 75), end_point=sd.get_point(x + 120, x + 75))


for _ in range(10):
    smile()

sd.pause()
