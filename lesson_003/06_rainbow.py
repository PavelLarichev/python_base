# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x, y = 50, 50
x1, y1 = 350, 450
for color in rainbow_colors:
    x += 5 # TODO помести 5-ку в переменную, т.к. ты используешь её несколько раз, и в width можно тоже её присваивать
    x1 += 5
    sp = sd.get_point(x, y)
    ep = sd.get_point(x1, y1)
    print(sd.line(start_point=sp, end_point=ep, color=color, width=4))
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

sd.pause()
