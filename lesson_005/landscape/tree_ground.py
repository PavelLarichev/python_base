# import simple_draw as sd
# sd.resolution = (1200, 1000)


def tree(point, angle, length, color):
    import simple_draw as sd
    from random import uniform
    if length < 4:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    next_point = v1.end_point
    angle_positive = angle + sd.random_number(18, 42)
    angle_negative = angle - sd.random_number(18, 42)
    next_length = length * uniform(.5, 1)
    tree(point=next_point, angle=angle_negative, length=next_length, color=(0, 255, 0))
    tree(point=next_point, angle=angle_positive, length=next_length, color=(0, 255, 0))
    sd.line(start_point=sd.get_point(0, 10), end_point=sd.get_point(1200, 10), width=55)


# root_point = sd.get_point(900, 30)
# tree(point=root_point, angle=90, length=65, color=(127, 63, 0))


# sd.pause()