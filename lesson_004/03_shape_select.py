# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = 800, 800


# def triangle(point, angle, length, color):
#     next_point = point
#     for angle in range(angle, angle + 240, 120):
#         v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
#         v1.draw(color=color)
#         next_point = v1.end_point
#     sd.line(start_point=next_point, end_point=point, width=2, color=color)
#
#
# def square(point, angle, length, color):
#     next_point = point
#     for angle in range(angle, angle + 270, 90):
#         v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
#         v1.draw(color=color)
#         next_point = v1.end_point
#     sd.line(start_point=next_point, end_point=point, width=2, color=color)
#
#
# def pentagon(point, angle, length, color):
#     next_point = point
#     for angle in range(angle, angle + 288, 72):
#         v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
#         v1.draw(color=color)
#         next_point = v1.end_point
#     sd.line(start_point=next_point, end_point=point, width=2, color=color)
#
#
# def hexagon(point, angle, length, color):
#     next_point = point
#     for angle in range(angle, angle + 300, 60):
#         v1 = sd.get_vector(start_point=next_point, angle=angle, length=length, width=2)
#         v1.draw(color=color)
#         next_point = v1.end_point
#     sd.line(start_point=next_point, end_point=point, width=2, color=color)


def figure(angle_number, point, length, color):
    degree = 360 // angle_number
    next_point = point
    for degree in range(0, degree * angle_number, degree):
        v1 = sd.get_vector(start_point=next_point, angle=degree, length=length, width=2)
        v1.draw(color=color)
        next_point = v1.end_point
    sd.line(start_point=next_point, end_point=point, width=2, color=color)


shapes_dict = {"1": {"shape_name": "triangle", "shape_func": 3},
               "2": {"shape_name": "square", "shape_func": 4},
               "3": {"shape_name": "pentagon", "shape_func": 5},
               "4": {"shape_name": "hexagon", "shape_func": 6}}


def user_input():
    print("Возможные фигуры:")
    for number, shape in shapes_dict.items():
        print(number, " - ", shape["shape_name"])
    while True:
        shape = input('Введите номер фигуры: ')
        if shape in shapes_dict:
            angle_number = shapes_dict[shape]["shape_func"]
            figure(angle_number=angle_number, point=sd.get_point(325, 300), length=125, color=sd.COLOR_BLACK)
            break
        else:
            print('Вы ввели некорректный номер:')
            continue


user_input()

sd.pause()
# Зачет!