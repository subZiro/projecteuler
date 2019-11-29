#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
_________________________________
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
"""



def f_factorial_n(n):
	# факториал числа n, вычисление при помощи рекурсии
	assert n >= 0, 'error n<0'

	if n == 0:
		return 1
	return f_factorial_n(n-1) * n


def f_sum_str(s):
	# функция принимает в качестве параметра число
	#возвращает сумму цифр в этом числе

	list_s = [int(elem) for elem in str(s)]
	return sum(list_s)


print(f_sum_str(f_factorial_n(100)))    # 648



