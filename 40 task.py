#!/usr/bin/python
# -*- coding: utf-8 -*-





"""
Дана иррациональная десятичная дробь, образованная объединением положительных целых чисел:

0.123456789101112131415161718192021...

Видно, что 12-ая цифра дробной части - 1.

Также дано, что dn представляет собой n-ую цифру дробной части. Найдите значение следующего выражения:

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""



def f_get_index(string, a):
	# функция возвразает число из строки string по индексу a, 
	# или список чисел если входная переменная a имеет тип список
	if type(a) is list:
		reslt = [int(string[elem]) for elem in a]
	else:
		reslt = string[a]
		
	return reslt


s = '0'
d_list = [1, 10, 100, 1000, 10000, 100000, 1000000]

i = 1
while len(s) <= d_list[-1]:
	s += str(i)
	i += 1


proizv = 1
for elem in f_get_index(s, d_list):
	proizv *= elem
print(proizv)   # 210




from functools import reduce
from operator import mul

product = reduce(mul, f_get_index(s, d_list))
print(product)   # 210



