# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.catfood = 30

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, уровень грязи {}'.format(
            self.food, self.money, self.dirt)


class Man:
    total_fullness = 0

    def __init__(self, name, house=None, stomach_capacity=30):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house
        self.stomach_capacity = stomach_capacity

    def __str__(self):
        return 'Я {}, мой уровень счастья {}, мой уровень сытости {}'.format(
            self.name, self.happiness, self.fullness)

    def eat(self):
        if self.house.food > self.stomach_capacity:
            self.fullness += self.stomach_capacity
            Man.total_fullness += self.stomach_capacity
            self.house.food -= self.stomach_capacity
            print('{} поел'.format(self.name))
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        cprint('Я {}, теперь у меня есть дом'.format(self.name), color='cyan')

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return False
        elif self.happiness <= 10:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
            return False
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness < 30:
            self.eat()
            return False
        return True


class Husband(Man):
    earned_money = 0

    def act(self):
        if self.house.money < 100:
            self.work()
        else:
            if super().act():
                dice = randint(1, 4)
                if dice == 1:
                    self.work()
                elif dice == 2:
                    self.eat()
                elif dice == 3:
                    self.pet_the_cat()
                else:
                    self.gaming()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        Husband.earned_money += 150

    def gaming(self):
        cprint('{} играл в WoT целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20


class Wife(Man):
    fur_coats_bought = 0

    def act(self):
        if self.house.food < 30:
            self.shopping()
        else:
            if super().act():
                dice = randint(1, 6)
                if dice == 1:
                    self.buy_fur_coat()
                elif dice == 2:
                    self.eat()
                elif dice == 3:
                    self.pet_the_cat()
                else:
                    self.clean_house()

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 80
            self.house.food += 65
            self.house.catfood += 15
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money > 350:
            cprint('{} купила шубу'.format(self.name), color='green')
            self.happiness += 60
            self.house.money -= 350
            Wife.fur_coats_bought += 1
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        self.fullness -= 10
        if self.house.dirt > 100:
            cprint('{} убралась дома'.format(self.name), color='green')
            self.house.dirt -= 100
        else:
            cprint('И так чисто, можно отдохнуть', color='green')

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# inhabitants = [serge, masha]
# for inhabitant in inhabitants:
#     inhabitant.go_to_the_house(house=home)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.dirt += 5
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#
# cprint('Всего съедено еды {}'.format(Man.total_fullness), color='yellow')
# cprint('Всего заработано денег {}'.format(Husband.earned_money), color='yellow')
# cprint('Всего куплено шуб {}'.format(Wife.fur_coats_bought), color='yellow')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, house=None, stomach_capacity=10):
        self.name = name
        self.fullness = 30
        self.house = house
        self.stomach_capacity = stomach_capacity

    def __str__(self):
        return 'Я {}, мой уровень сытости {}'.format(
            self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return False
        if self.fullness < 20:
            self.eat()
        dice = randint(1, 4)
        if dice == 1:
            self.soil()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.catfood > 10:
            self.house.catfood -= self.stomach_capacity
            self.fullness += 20
            print('{} поел'.format(self.name))
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спал весь день'.format(self.name), color='green')
        self.fullness -= 10

    def soil(self):
        cprint('{} драл обои'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5

    def go_to_the_house(self, house):
        self.house = house
        cprint('Я {}, теперь у меня есть дом'.format(self.name), color='cyan')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __init__(self, name, stomach_capacity=10):
        super().__init__(name=name)
        self.happiness = 100
        self.stomach_capacity = stomach_capacity

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        else:
            self.sleep()

    def sleep(self):
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

inhabitants = [serge, masha, kolya, murzik]
for inhabitant in inhabitants:
    inhabitant.go_to_the_house(house=home)


for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirt += 5
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
# Зачет!