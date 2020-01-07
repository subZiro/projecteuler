#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
____________________________

В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Сколькими разными способами можно составить £2, используя любое количество монет?
"""



def f_count_solutions(list, total):
	# рекурсивная функция принимает список монет и число которую нужно получить из списка монет
	if len(list) == 0:
		if total == 0:
			return 1
		else:
			return 0

	x = 0 
	reslt = 0

	while x*list[0] <= total:
		reslt += f_count_solutions(list[1:], total - x*list[0])
		x += 1
	return reslt



money_list = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200

print(f_count_solutions(money_list, total))    #73682

