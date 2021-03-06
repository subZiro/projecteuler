#!/usr/bin/python
# -*- coding: utf-8 -*-



"""
Десятичное число 585(10) = 1001001001(2) (в двоичной системе), является палиндромом по обоим основаниям.

Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.
(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).
"""



def f_numbr_is_palindrom(a):
	# функция возыращает истину если переданное число является палиндромом
	return True if str(a) == str(a)[::-1] else False


n = 1000000
k = 0 

for i in range(1, n):
	if f_numbr_is_palindrom(i) and f_numbr_is_palindrom(bin(i)[2:]):
		k += i 
		
print(k)    #872187



