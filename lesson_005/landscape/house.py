# import simple_draw as sd
# sd.resolution = (1200, 1000)

def wall():
    import simple_draw as sd
    sd.line(start_point=sd.get_point(450, 0), end_point=sd.get_point(450, 300), width=2, color=(255, 255, 0))
    sd.line(start_point=sd.get_point(850, 0), end_point=sd.get_point(850, 300), width=2, color=(255, 255, 0))
    step = 500
    for y in range(0, 300, 50):
        y1 = y + 50
        step -= 50
        if step == 400:
            step = 500
        for x in range(step, 800, 100):
            x1 = x + 100
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x1, y1)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=(255, 255, 0), width=2)


# wall()


def roof():
    import simple_draw as sd
    x1 = 450
    x2 = 850
    for y in range(300, 505, 5):
        sd.line(start_point=sd.get_point(x1, y), end_point=sd.get_point(x2, y), width=5, color=(255, 0, 0))
        x1 += 5
        x2 -= 5


# roof()


def window():
    import simple_draw as sd
    sd.square(left_bottom=sd.get_point(600, 100), side=125, color=(255, 255, 255), width=0)


# window()


# sd.pause()