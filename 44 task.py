#!/usr/bin/python
# -*- coding: utf-8 -*-



"""
_________________________________
Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. 
Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.

Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность являются пятиугольными числами 
и значение D = |Pk − Pj| минимально, и дайте значение D в качестве ответа.
"""


def f_penta_numbers():
	# 
	n = 1
	while True:
		p = int(n*(3*n-1)/2)
		yield p
		n += 1


def f_sum_dif_pentagonal():
	#
	sd_penta = set()
	for i in pents_num_list:
		for j in pents_num_list:
			if i+j in pents_num_list and abs(i-j) in pents_num_list:
				sd_penta.add(abs(i-j))
	return min(sd_penta)


pent = f_penta_numbers()

from itertools import islice
pents_num_list = list(islice(pent, 10000000))

print(f_sum_dif_pentagonal())   # 5482660

