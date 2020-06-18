# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = 800, 800


def triangle(point, angle, length, color):
    next_point = point
    for angle in range(angle, angle + 240, 120):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
        v1.draw(color=color)
        next_point = v1.end_point
    sd.line(start_point=next_point, end_point=point, width=2, color=color)


def square(point, angle, length, color):
    next_point = point
    for angle in range(angle, angle + 270, 90):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
        v1.draw(color=color)
        next_point = v1.end_point
    sd.line(start_point=next_point, end_point=point, width=2, color=color)


def pentagon(point, angle, length, color):
    next_point = point
    for angle in range(angle, angle + 288, 72):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
        v1.draw(color=color)
        next_point = v1.end_point
    sd.line(start_point=next_point, end_point=point, width=2, color=color)


def hexagon(point, angle, length, color):
    next_point = point
    for angle in range(angle, angle + 300, 60):
        v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
        v1.draw(color=color)
        next_point = v1.end_point
    sd.line(start_point=next_point, end_point=point, width=2, color=color)


def user_input():
    # TODO тут можно сделать словарь, в котором будет ключ - номер фигуры,
    #  а значение - словарь, который бы содержал название
    #  фигуры и функцию фигуры, потом ты сможешь из этого
    #  словаря достать сразу ф-ию фигуры и вызвать, тем более,
    #  что у тебя в ф-ии передаются одни и те же параметры.
    #  Точнее будут передаватьсяя, когда сделаешь расчет
    #  угла по их кол-ву, как я написал в первом задании.
    print('Возможные фигуры:\n0 : треугольник \n1 : квадрат \n2 : ппятиугольник \n3 : шестиугольник \n')
    number_input = input('Введите желаемую фигуру: ')
    figure = int(number_input)
    if figure == 0:
        triangle(point=sd.get_point(350, 300), angle=45, length=175, color=sd.COLOR_DARK_GREEN)
    elif figure == 1:
        square(point=sd.get_point(400, 300), angle=62, length=150, color=sd.COLOR_DARK_GREEN)
    elif figure == 2:
        pentagon(point=sd.get_point(400, 300), angle=41, length=100, color=sd.COLOR_DARK_GREEN)
    elif figure == 3:
        hexagon(point=sd.get_point(475, 320), angle=88, length=100, color=sd.COLOR_DARK_GREEN)
    else:
        print('Вы ввели некорректный номер:')


user_input()

sd.pause()
