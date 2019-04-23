#!/usr/bin/python
# -*- coding: utf-8 -*-

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
________________
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""

def f_issimple(n):
	# функция возвращает истину, если входное число является простым, и ложь в противном случае. 
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

n = 2
i = 1

while i <= 10001:
	if f_issimple(n):
		i += 1
	n += 1

print(n-1)



