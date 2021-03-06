#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
____________________________________
Идеальным числом называется число, у которого сумма его делителей равна самому числу. 
Например, сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28, что означает, 
что число 28 является идеальным числом.

Число n называется недостаточным, если сумма его делителей меньше n, 
и называется избыточным, если сумма его делителей больше n.

Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16), 
наименьшее число, которое может быть записано как сумма двух избыточных чисел, равно 24. 

Используя математический анализ, можно показать, 
что все целые числа больше 28123 могут быть записаны как сумма двух избыточных чисел. 
Эта граница не может быть уменьшена дальнейшим анализом, даже несмотря на то, что наибольшее число, 
которое не может быть записано как сумма двух избыточных чисел, меньше этой границы.

Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел.
'''


def f_is_abundant(n):
	'''функция принимает число-n, True если число является избыточным 
	(сумма делитеоей n > самого числа n) 
	'''
	triangle_list = []
	for i in range(1, int((n ** 0.5))+1):
		if n % i == 0:
			triangle_list.append(i)
			triangle_list.append(int(n/i))
	return (sum(triangle_list) - n) > n 
	

def main():
	#список избыточных чисел
	abundants_list = [i for i in range(1, 28123) if f_is_abundant(i)]
	r_list = []
	for i in range(1, 28123):
		for elem in abundants_list:
			if elem >= i and f_is_abundant(elem+i):
				r_list.append(i)
	print(r_list)


if __name__ == '__main__':
	main()
