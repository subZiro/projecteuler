#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
__________________________________________
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 2^1000?"""


user_input = 1000

x = str(2 ** user_input)  
x_list = [int(elem) for elem in x]

print(sum(x_list))