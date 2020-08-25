# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
import random

_holder = []


def guess_number():
    global _holder
    _holder = list(range(0, 10))
    random.shuffle(_holder)
    if _holder[0] == 0:
        guess_number()
    else:
        _holder = _holder[:4]


def predict():
    counter = 0
    while True:
        number = list(input("Загадай число"))
        if len(number) != 4:
            print("Вы ввели неверное число")
            continue
        else:
            is_unique(number)
            cows = 0
            bulls = 0
            for i in range(len(_holder)):
                if str(number[i]) == str(_holder[i]):
                    bulls += 1
                elif (number[i]) in str(_holder):
                    cows += 1
            counter += 1
            print("количество коров:", cows, ", количество быков:", bulls)
            if bulls == 4:
                print("Вы выиграли! Колчиество ходов:", counter)
                is_gameover()
            else:
                continue


def is_unique(number):
    while True:
        number = number
        setnumber = set(number)
        if len(number) == len(setnumber) == 4:
            return number
        else:
            print("Вы ввели неверное число,")
            break


def is_gameover():
    import sys
    while True:
        new_game = input("Хотите начать новую игру? y/n")
        if new_game == "y":
            guess_number()
            predict()
        elif new_game == "n":
            print("Игра окончена")
            sys.exit()
        else:
            print("Введена неверная команда")
            continue

