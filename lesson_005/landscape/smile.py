# import simple_draw as sd
# sd.resolution = (1200, 1000)


def smile(x, y):
    import simple_draw as sd
    sd.circle(center_position=sd.get_point(x, y), radius=50, width=3)
    sd.circle(center_position=sd.get_point(x - 20, y + 20), radius=10,  width=3)
    sd.circle(center_position=sd.get_point(x + 25, y + 20), radius=10,  width=3)
    sd.line(start_point=sd.get_point(x - 20, y - 25), end_point=sd.get_point(x + 20, y - 25),  width=3)
    sd.pause()