#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2. For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
_________________
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a2 + b2 = c2. Например, 32 + 42 = 9 + 16 = 25 = 52.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""

def f_tripl_pifagor(sum_abc):
	#функция принимает сумму чисел a,b,c и возвращает значение каждого числа в виде кортежа.
	for a in range(2, 500):
		for b in range(2, 500):
			if (1000 - a - b)**2 == b*b + a*a:
				return a * b * (1000 - a - b)

print('a*b*c = %d' % f_tripl_pifagor(1000))   # 31875000
