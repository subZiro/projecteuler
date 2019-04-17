#!/usr/bin/python
# -*- coding: utf-8 -*-

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
______________________
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

def f_Nom(x):
	list_dev = [11, 12, 13, 14, 16, 17, 18, 19, 20]
	k = 0
	for i in list_dev:
		if not x % i:
			k += 1
		else:
			break
	if k == len(list_dev):
		return True
	else:
		return False

i_start = 0
i_bool = True

while True:
	i_start += 11
	if f_Nom(i_start):
		break

print(i_start)



