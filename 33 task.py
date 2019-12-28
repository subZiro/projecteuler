#!/usr/bin/python
# -*- coding: utf-8 -*-



"""

____________________________________

Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее, 
будет ошибочно полагать, что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.

Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.

Существует ровно 4 нетривиальных примера дробей подобного типа, 
которые меньше единицы и содержат двухзначные числа как в числителе, так и в знаменателе.

Пусть произведение этих четырех дробей дано в виде несократимой дроби 
(числитель и знаменатель дроби не имеют общих сомножителей). Найдите знаменатель этой дроби.

"""


def f_solution_1():
	#  фунуция возвращает произведение 4 знаменателей
	d = 1 
	for i in range(1, 10):
	    for j in range(1, i):
	        q, r = divmod(9*j*i, 10*j-i)
	        if not r and q <= 9:
	            d *= i/float(j)

	return d   

print(f_solution_1())  # 100
print('---------')









import math
def f_solution_2():
	#  фунуция возвращает произведение 4 знаменателей
	dp = 1
	np = 1
	for c in range(1, 10):
		for d in range(1, c):
			for n in range(1, d):
				if ((n * 10 + c) * d == (c * 10 + d) * n):
					np*= n
					dp*= d
	return dp / math.gcd(np, dp)


print(f_solution_2())   # 100
