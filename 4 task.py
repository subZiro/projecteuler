#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
__________________

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

"""

def f_isPalindrom(x):
	return str(x) == str(x)[::-1]

def f_maxPalindrom():
	max_pal = 0
	for i in range(500, 1000):
		for j in range(500, 1000):
			if f_isPalindrom(i*j) and i * j > max_pal:
				max_pal = i * j
	return max_pal
	
print(f_maxPalindrom())




	
