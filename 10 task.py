#!/usr/bin/python
# -*- coding: utf-8 -*-

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
_______________
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""


'''
# второе имя этого алгоритма скорость
def f_issimple(n):
	# функция возвращает истину, если входное число является простым, и ложь в противном случае. 
	for i in range(2, (n ** 0.5) + 1):
		if n % i == 0:
			return False

	return True

def f_sum_simple(n_lim):
	sum_simple = 2
	for i in range(3, n_lim, ++2):
		if f_issimple(i):
			sum_simple += i
	
	return sum_simple


print(f_sum_simple(2000000))   #142913828922
'''




def f_issimple_list(n):
	# функция принимает число и возвращает сумму простых первых n-чисел 
	# создается список длинной n-элементов 
	simp_list = list(range(n+1))
	simp_list[1] = 0   # 1-не является простым числом, обнуляем

	for i in simp_list[2:]:   
		for j in range(i+i, len(simp_list), i):
			simp_list[j] = 0    # обнуляем элементы кратные i, начиная с i*2 элемента

	return sum(simp_list)



print(f_issimple_list(2000000))      #142913828922