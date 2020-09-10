# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Magic:
    def __str__(self):
        return 'Магия'

    def __add__(self, other):
        if isinstance(other, Air):
            return AirElemental()
        elif isinstance(other, Fire):
            return FireElemental()
        elif isinstance(other, Earth):
            return EarthElemental()
        elif isinstance(other, Water):
            return WaterElemental()
        else:
            return None


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()


class Storm:

    def __init__(self):
        self.elem1 = Air()
        self.elem2 = Water()

    def __str__(self):
        return 'Шторм'


class Steam:

    def __init__(self):
        self.elem1 = Water()
        self.elem2 = Fire()

    def __str__(self):
        return 'Пар'


class Mud:

    def __init__(self):
        self.elem1 = Water()
        self.elem2 = Earth()

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __init__(self):
        self.elem1 = Fire()
        self.elem2 = Air()

    def __str__(self):
        return 'Молния'


class Dust:

    def __init__(self):
        self.elem1 = Earth()
        self.elem2 = Air()

    def __str__(self):
        return 'Пыль'


class Lava:

    def __init__(self):
        self.elem1 = Fire()
        self.elem2 = Earth()

    def __str__(self):
        return 'Лава'


class FireElemental:

    def __init__(self):
        self.elem1 = Magic()
        self.elem2 = Fire()

    def __str__(self):
        return 'Огненный элементаль'


class AirElemental:

    def __init__(self):
        self.elem1 = Magic()
        self.elem2 = Air()

    def __str__(self):
        return 'Элементаль воздуха'


class WaterElemental:

    def __init__(self):
        self.elem1 = Magic()
        self.elem2 = Water()

    def __str__(self):
        return 'Водный элементаль'


class EarthElemental:

    def __init__(self):
        self.elem1 = Magic()
        self.elem2 = Earth()

    def __str__(self):
        return 'Элементаль земли'


print(Water(), '+', Air(), '=', Air() + Water())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Magic(), '+', Air(), '=', Magic() + Air())
print(Water(), '+', Magic(), '=', Magic() + Water())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
# Зачет!