#!/usr/bin/python
# -*- coding: utf-8 -*-




'''
__________________________________________


'''


'''
def factrial(n):
	prod = 1
	for i in range(1, n+1):
		prod *= i
	return prod


print(factrial(9))
'''

def f_factorial_0to9():
	# функция возвращает список содержащий факториалы чисел от от 0 до 9 

	reslt = [1]*10
	for i in range(1,10):
		reslt[i] = reslt[i-1]*i

	return reslt



def f_komb(n):
	#
	dec_list = [i for i in range(10)]
	reslt = ''
	n -= 1

	for i in range(len(dec_list)-1, -1, -1):
		t = int(n/fact_list[i])
		n %= fact_list[i]
		reslt += str(dec_list[t])
		dec_list.pop(t)
	return reslt 





fact_list = f_factorial_0to9()

print(f_komb(1000000))   #2783915460





