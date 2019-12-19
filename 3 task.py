#!/usr/bin/python
# -*- coding: utf-8 -*-

"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
____________________
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

"""

import math

def f_list_smpl_div(x):
	list_smpldiv = []
	xsqrt = int(math.ceil(math.sqrt(x)))

	for i in range(2, xsqrt):
		if x % i == 0:
			if f_list_smpl_div(i) == []:
				list_smpldiv.append(i)
	return list_smpldiv

a_inpt = 600851475143

max_elem = f_list_smpl_div(a_inpt)

print(max(max_elem))   #6857
