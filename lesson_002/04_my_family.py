#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["father", "mother", "son"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [[my_family[0], 170], [[my_family[1]], 155], [my_family[2], 90]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца -", my_family_height[0][1], "см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
summary_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print("Рост семьи -", summary_height, "см")