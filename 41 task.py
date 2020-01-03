#!/usr/bin/python3
# -*- coding: utf-8 -*-



""""
___________________________________________

Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до n используется в нем ровно один раз. 
К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?

"""



def f_issimple_list(n):
	# функция принимает число и возвращает сумму простых первых n-чисел 
	# создается список длинной n-элементов 
	simp_list = list(range(n*n))
	simp_list[1] = 0   # 1-не является простым числом, обнуляем

	for i in simp_list[2:]:   
		for j in range(i+i, len(simp_list), i):
			simp_list[j] = 0    # обнуляем элементы кратные i, начиная с i*2 элемента

	#simp_list = list(set(simp_list))[1:]
	#simp_list.sort()

	return simp_list



def f_is_pandigital(n, s): 
	# функция возвращает True, если число - n является пан-цифровым
	# и каждая из цифр [1:s] используется в нем только раз

	n = str(n)
	return len(n)==s and not '1234567890'[:s].strip(n)




simp_list = f_issimple_list(99999)
max_pandigit = 0


for i in range(5, 10):

	simp_list_in = simp_list[10**(i-2) : 10**i]

	simp_list_in = list(set( simp_list_in ))
	simp_list_in.sort()
	
	tmp_list = [elem for elem in simp_list_in if f_is_pandigital(elem, i)]

	if tmp_list and max(tmp_list) > max_pandigit:
		max_pandigit = max(tmp_list)



print(max_pandigit)   #7652413


