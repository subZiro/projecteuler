#!/usr/bin/python
# -*- coding: utf-8 -*-




'''
___________________________________________________
Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

Можно убедиться, что сумма чисел в диагоналях равна 101.

Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?

'''



import numpy as np 



def f_print_matrix_NN(array):
	# варианты выводов на экран двумерной матрицы
	'''
	for x in list(zip(*r)):
	        print(*x)
	print('----------')

	# вывод без форматирования 
	for x in r:
		print(*x)
	'''	
	# вывод с форматированием
	print('----------')
	for i in range(len(array)):
		for j in range(len(array[i])):
			print("%6s" % array[i][j], end = '')
		print()
	print('----------')

	
def f_array_snake(n):
	# функция принимет размерность квадратной матрицы и заполняет ее по спирали от края к центру
	# и возвращает получену матрицу
	# заполнение происходит с [0,0]>>[1,0]>>[2,0]>> и тд
    dx, dy = 0, -1
    x, y = 0, 0

    arr = [[0] * n for _ in range(n)]

    for i in range(n**2, 0, -1):
        arr[x][y] = i
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x+dx, y+dy
    
    return arr


def f_sum_diag_matrix(array):
	# функция принимет двумерный массив и возвращает сумму 2 диагоналей 

	s1 = np.diagonal(array)
	s2 = np.fliplr(array).diagonal()

	return sum(np.hstack((s1[:N//2], s1[N//2+1:], s2)))






N = 1001
r = np.array(f_array_snake(N))
#f_print_matrix_NN(r)
print(f_sum_diag_matrix(r))   #669171001


