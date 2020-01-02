#!/usr/bin/python
# -*- coding: utf-8 -*-




"""

Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c},
то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?

"""


def f_is_triple(a, b, c):
	# функция принимает 3 числа и возвращает True если полученая фигура является прямоугольным треугольником
	# иначе False
	if (max(a,b,c) <= (a+b+c) - max(a,b,c)) and \
	(max(a,b,c)**2 == a**2 + b**2 + c**2 - max(a,b,c)**2):
		return True
	else:
		return False



k = 0
p_k = 0


for p in range(120, 1000):
	triple = []

	for a in range(1, p):

		tmp = []
		for b in range(1, p-a):

			if f_is_triple(a, b, p-(a+b)):
				tmp.append(a)
				tmp.append(b)
				tmp.append(p - (a+b))
				tmp.sort()
				
		if tmp and tmp not in triple:
			triple.append(tmp)

	triple = [set(line) for line in triple]

	if len(triple) > k:
		k = len(triple)
		p_k = p





print(p_k, k)   # 840 9

