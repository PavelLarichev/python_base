# -*- coding: utf-8 -*-

import simple_draw as sd


import random

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(point, radius=radius)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет


def bubble(point, step, color, width):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius=radius, color=color, width=width)


# Нарисовать 10 пузырьков в ряд


# for x in range(100, 1001, 100):
#     point = sd.get_point(x, 100)
#     bubble(point=point, step=5, color=sd.random_color(), width=2)

# Нарисовать три ряда по 10 пузырьков
#
# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5, color=sd.random_color(), width=2)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=random.randint(1, 10), color=sd.random_color(), width=random.randint(1, 3))

sd.pause()

# зачет!
