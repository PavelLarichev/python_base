# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

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


def all_figures():
    color = user_input()
    figure(angle_number=3, point=sd.get_point(200, 200), length=175, color=color)
    figure(angle_number=4, point=sd.get_point(550, 100), length=150, color=color)
    figure(angle_number=5, point=sd.get_point(200, 500), length=100, color=color)
    figure(angle_number=6, point=sd.get_point(600, 500), length=100, color=color)


color_dict = {'1': {"color_name": "red", "color_code": sd.COLOR_RED},
              '2': {"color_name": "orange", "color_code": sd.COLOR_ORANGE},
              '3': {"color_name": "yellow", "color_code": sd.COLOR_YELLOW},
              '4': {"color_name": "green", "color_code": sd.COLOR_GREEN},
              '5': {"color_name": "cyan", "color_code": sd.COLOR_CYAN},
              '6': {"color_name": "blue", "color_code": sd.COLOR_BLUE},
              '7': {"color_name": "purple", "color_code": sd.COLOR_PURPLE}}


def user_input():
    print("Возможные цвета:")
    for number, color in color_dict.items():
        print(number, " - ", color["color_name"])
    while True:
        color = input('Введите желаемй цвет: ')
        if color in color_dict:
            color = color_dict[color]["color_code"]
            return color
        else:
            print('Вы ввели некорректный номер:')
            continue


all_figures()

sd.pause()
# Зачет!