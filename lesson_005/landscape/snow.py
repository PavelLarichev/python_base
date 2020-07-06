# import simple_draw as sd
# sd.resolution = (1200, 1000)


def snow():
    import simple_draw as sd
    for y in range(100, 900, 100):
        x = sd.random_number(100, 300)
        sd.snowflake(center=sd.get_point(x, y), length=50)


# snow()