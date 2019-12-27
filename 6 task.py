#!/usr/bin/python
# -*- coding: utf-8 -*-

"""The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

_______________________________________

Сумма квадратов первых десяти натуральных чисел равна
1**2 + 2**2 + ... + 10**2 = 385
Квадрат суммы первых десяти натуральных чисел равен
(1 + 2 + ... + 10)**2 = 55**2 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
"""

def f_sum_sqrt(n):
	#1**2 + 2**2 + ... + 10**2  = n(n + 1)(2n + 1)/6
	return (n * (n + 1) * (2*n + 1)) / 6

def f_sqrt_sum(n):
		#(1 + 2 + ... + 10)**2 = n(n + 1) / 2
		return (n * (n + 1) / 2) ** 2

sizeN = 100
print(round(f_sqrt_sum(sizeN) - f_sum_sqrt(sizeN)))    # 25164150






