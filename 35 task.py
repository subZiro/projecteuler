#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца 
в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?
"""





def f_issimple_list(n):
	# функция принимает число и возвращает сумму простых первых n-чисел 
	# создается список длинной n-элементов 
	simp_list = list(range(n))
	simp_list[1] = 0   # 1-не является простым числом, обнуляем

	for i in simp_list[2:]:   
		for j in range(i+i, len(simp_list), i):
			simp_list[j] = 0    # обнуляем элементы кратные i, начиная с i*2 элемента

	return list(set(simp_list))



n = 1000000


simpl_list = f_issimple_list(n)
print('len = ', len(simpl_list))


k = 0
for i in range(2, n):

	flg = True
	for j in range(len(str(i))):
		i = str(i)[1:] + str(i)[0]
		if int(i) not in simpl_list:
			flg = False
			break
	
	if flg: 
		k += 1
		print(k)
		

print('k=', k)    #55
