#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
_____________________________________

Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:

Треугольные	 	    Tn=n(n+1)/2	 	    1, 3, 6, 10, 15, ...
Пятиугольные	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Шестиугольные	 	Hn=n(2n−1)	 	    1, 6, 15, 28, 45, ...
Можно убедиться в том, что T285 = P165 = H143 = 40755.

Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.
"""



def f_triangular_numbers():
	# функци генерации треугольных чисел
	n = 1
	while True:
		p = int(n*(n + 1)/2)
		yield p
		n += 1

def f_pentagonal_numbers():
	# функция генерации пятиугольных чисел
	n = 1
	while True:
		p = int(n*(3*n - 1)/2)
		yield p
		n += 1

def f_hexagonal_numbers():
	# функция генерауии шестиугольных чисел
	n = 1
	while True:
		p = int(n*(2*n - 1))
		yield p
		n += 1


from itertools import islice


triple_num_list = list(islice(f_triangular_numbers(), 1000000))
pentas_num_list = list(islice(f_pentagonal_numbers(), 1000000))
hexa_num_list = list(islice(f_hexagonal_numbers(), 1000000))


for elem in triple_num_list[200:]:
	if elem in pentas_num_list and elem in hexa_num_list:
		break
print(elem)   # 1533776805




