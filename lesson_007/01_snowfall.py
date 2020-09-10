# -*- coding: utf-8 -*-

import simple_draw as sd

N = 10
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.length = 30
        self.speed = sd.random_number(10, 30)
        self.x = sd.random_number(50, 600)
        self.y = sd.random_number(500, 600)
        self.color = sd.COLOR_YELLOW

    def draw(self, color):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=color)

    def move(self):
        self.y -= self.speed

    def can_fall(self):
        if self.y <= 20:  # TODO self.y <= 20 уже бул
            return True


flake = Snowflake()


def get_flakes():
    snowflakes = []
    for i in range(0, N):
        snowflakes.append(Snowflake())
    return snowflakes


def get_fallen_flakes():
    snowflakes = []
    for i in range(0, len(flakes)):
        if flake.can_fall():
            snowflakes.append(i)
    return snowflakes


def append_flakes(fallen_flakes):
    for i in range(0, len(fallen_flakes)):
        if flake.can_fall():
            flakes.append(Snowflake())


# while True:
#     flake.draw(sd.background_color)
#     if not flake.can_fall():
#         flake.move()
#         flake.draw(sd.COLOR_YELLOW)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
flakes = get_flakes()
while True:
    for flake in flakes:
        flake.draw(color=sd.background_color)
        if not flake.can_fall():
            flake.move()
        flake.draw(sd.COLOR_WHITE)
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
