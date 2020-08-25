# -*- coding: utf-8 -*-

import simple_draw as sd


snowflakes_dict = {}
snowflakes_list = []
length_list = []
point_list = []
N = 10


def create_snowflakes():
    global length_list, N, snowflakes_dict, snowflakes_list
    snowflakes_dict = {i: [sd.random_number(0, 500), 500, i] for i in range(N)}
    for i in range(N):
        snowflakes_list = [[snowflakes_dict[key][0], snowflakes_dict[key][1]] for key, val in snowflakes_dict.items()]
        length_num = sd.random_number(10, 100)
        length_list.append(length_num)
        return snowflakes_dict, snowflakes_list


def draw_snowflake():
    global N
    while True:
        sd.start_drawing()
        for i in range(N):
            length = 50
            if len(snowflakes_list) < N:
                sd.snowflake(center=snowflakes_list[i], length=length, color=sd.background_color)
            x, y, delay = snowflakes_dict[i]
            if delay < 1:
                point = sd.get_point(x, y)
                point1 = sd.get_point(snowflakes_list[i][0], snowflakes_list[i][1])
                sd.snowflake(center=point1, length=length, color=sd.background_color)
                snowflakes_dict[i][1] -= 10
                sd.snowflake(center=point, length=length)
                snowflakes_list[i] = [x, y]
                # sd.clear_screen()
                if y < 20:
                    snowflakes_dict[i][1] = 500
                    continue
            snowflakes_dict[i][2] -= .2
            sd.finish_drawing()
            sd.sleep(0.01)
        if sd.user_want_exit():
            break