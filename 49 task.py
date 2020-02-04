#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
________________________
Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330, 
необычна в двух отношениях: (1) каждый из трех членов является простым числом, 
(2) все три четырехзначные числа являются перестановками друг друга.

Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных простых чисел, 
демонстрирующих это свойство. Однако, существует еще одна четырехзначная возрастающая арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена этой прогрессии?
"""

from itertools import permutations


def f_issimple_list(n):
	'''функция принимает число и возвращает сумму простых первых n-чисел 
	создается список длинной n-элементов 
	'''
	simp_list = list(range(n))
	simp_list[1] = 0   # 1-не является простым числом, обнуляем
	for i in simp_list[2:]:   
		for j in range(i+i, len(simp_list), i):
			simp_list[j] = 0    # обнуляем элементы кратные i, начиная с i*2 элемента
	simp_list = [elem for elem in simp_list if elem > 1487 and elem < 10000]
	return simp_list


def f_diff_of_permutat(array):
	'''функция принимает массив и возвращает конкатенированную строку элементов если они 
	образуют возрастающую арифметическую прогрессию
	'''
	if len(array) < 3:
		return False
	array.sort()
	for i in range(len(array)):
		for j in range(i+1, len(array)):

			d = array[j] - array[i]
			if array[j] + d in array:
				return str(array[i]) + str(array[j]) + str(array[j]+d)
	return False


def main():
	p_list = f_issimple_list(10000)

	for elem in p_list:
	    p = permutations(str(elem), 4)
	    a = [int(''.join(x)) for x in p]  # создание списка перестановок простого числа
	    a = list(set([x for x in a if x in p_list]))  # удаление всех повторений перестановок и не простых чисел

	    if f_diff_of_permutat(a):
	   		print(f_diff_of_permutat(a))
	   		break


if __name__ == '__main__':
	main()   # 296962999629