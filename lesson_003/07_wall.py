# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

step = 0
for y in range(0, 1000, 50):
    y1 = y + 50
    step -= 50
    if step == - 100:
        step = 0
    for x in range(step, 1000, 100):
        x1 = x + 100
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=(127, 63, 0), width=2)
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()

# зачет!
