#!/usr/bin/python
# -*- coding: utf-8 -*-



"""Число 3797 обладает интересным свойством. Будучи само по себе простым числом, 
из него можно последовательно выбрасывать цифры слева направо, 
число же при этом остается простым на каждом этапе: 3797, 797, 97, 7. 
Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.

Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево, 
так и слева направо, но числа при этом остаются простыми.

ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.
"""



def f_issimple_list(n):
	# функция принимает число и возвращает сумму простых первых n-чисел 
	# создается список длинной n-элементов 
	simp_list = list(range(n))
	simp_list[1] = 0   # 1-не является простым числом, обнуляем

	for i in simp_list[2:]:   
		for j in range(i+i, len(simp_list), i):
			simp_list[j] = 0    # обнуляем элементы кратные i, начиная с i*2 элемента

	return list(set(simp_list))[1:]



simpl_list = f_issimple_list(1000000)
simpl_list.sort()



sum_reslt = 0 

for elem in simpl_list[4:]:

	flg = True
	elem_rght = elem
	elem_lft = elem
	for j in range( len( str(elem) )-1 ):

		elem_rght = elem_rght//10
		elem_lft = int( str(elem_lft)[1:] )
	
		if elem_rght not in simpl_list or elem_lft not in simpl_list:
			flg = False
			break

	if flg:
		sum_reslt += elem





print(sum_reslt)   #748317









