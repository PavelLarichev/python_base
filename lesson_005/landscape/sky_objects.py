# import simple_draw as sd
# sd.resolution = (1200, 1000)


def rainbow():
    import simple_draw as sd
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    radius = 2000
    for color in rainbow_colors:
        radius -= 20
        sd.circle(center_position=sd.get_point(-300, -500), radius=radius, color=color, width=20)


# rainbow()


def sun():
    import simple_draw as sd
    point = sd.get_point(400, 800)
    sd.circle(center_position=sd.get_point(400, 800), width=0, radius=75)
    for angle in range(0, 360, 60):
        v = sd.get_vector(start_point=point, angle=angle, length=150)
        v.draw(width=7)


# sun()
# sd.pause()