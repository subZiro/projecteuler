#!/usr/bin/python
# -*- coding: utf-8 -*-



"""
_____________________________________
Последовательность треугольных чисел образуется путем сложения натуральных чисел. 
К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...


Перечислим делители первых семи треугольных чисел:
 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?
"""

def f_l_div_triangle(n):
	# функция принимает число-n, возвращает список делителей этого числа 
	triangle_list = []

	for i in range(1, int((n ** 0.5))+1):
		if n % i == 0:
			triangle_list.append(i)
			triangle_list.append(int(n/i))

	return triangle_list


i = 1
k = 0

while k <= 500:	
	# нахождение треугольного числа n = (n+1)n/2
	triangle_nums = i/2 * (i+1)
	k = len(f_l_div_triangle(triangle_nums))
	i += 1


print(f_l_div_triangle(triangle_nums)[1])    # 76576500




