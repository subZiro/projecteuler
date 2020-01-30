#!/usr/bin/python
# -*- coding: utf-8 -*-




"""
_________________________________

Первые два последовательные числа, каждое из которых имеет два отличных друг от друга простых множителя:

14 = 2 × 7
15 = 3 × 5

Первые три последовательные числа, каждое из которых имеет три отличных друг от друга простых множителя:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Найдите первые четыре последовательных числа, каждое из которых имеет четыре отличных друг от друга простых множителя. Каким будет первое число?
"""


#134043


def f_issimple_list(n):
	# функция принимает число и возвращает сумму простых первых n-чисел 
	# создается список длинной n-элементов 
	simp_list = list(range(n))
	simp_list[1] = 0   # 1-не является простым числом, обнуляем

	for i in simp_list[2:]:   
		for j in range(i+i, len(simp_list), i):
			simp_list[j] = 0    # обнуляем элементы кратные i, начиная с i*2 элемента

	simp_list = list(set(simp_list))[1:]
	simp_list.sort()

	return simp_list



def f_prime_factors(numb):
	# фунеция на вход принимает число и разбивает его на простые множители 
	factors_list = list()

	while numb % 2 == 0 :   # делим число на 2 пока оно делится на цело на 2
		factors_list.append(2)
		numb /= 2

	for p in range(3, int(numb + 1), 2):   #  оставшееся число разбиваем на простые множители
		if numb % p == 0 and p in p_list:
			factors_list.append(p)

	
	
	return factors_list





p_list = f_issimple_list(100000)

cons = 4
result = []
i = 1

while len(result) < cons:
	prime = set(f_prime_factors(i))

	if len(prime) == cons:
		result.append(i)
	else:
		result = []

	i += 1


print(*result)   # 134043 134044 134045 134046







