#!/usr/bin/python
# -*- coding: utf-8 -*-



"""
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""

def f_factorial_0to9():
	# функция возвращает список содержащий факториалы чисел от от 0 до 9 
	reslt = [1]*10
	for i in range(1,10):
		reslt[i] = reslt[i-1]*i
	return reslt



factorial = f_factorial_0to9()

sum_reslt = 0

for i in range(3, 10000000):
	sum_elem = 0 
	for elem in str(i):
		sum_elem += factorial[int(elem)]

	if sum_elem == i:
		sum_reslt += sum_elem

print(sum_reslt)










