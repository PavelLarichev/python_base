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
    # sd.clear_screen()
    for i in range(N):
        point = sd.get_point(x_list[i], y_list[i])
        length = length_list[i]
        sd.snowflake(center=point, length=length, color=sd.background_color)
        y_list[i] -= 65
        if y_list[i] <= 50:
            break
        point1 = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point1, length=length, color=sd.COLOR_WHITE)
        sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

