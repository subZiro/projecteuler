#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
___________________________________________
Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), 
текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. Начните с сортировки в алфавитном порядке. 

Затем подсчитайте алфавитные значения каждого имени и 
умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) 
является 938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
'''




alpha_dict = {}
for i in range(65, 91):
    alpha_dict[chr(i)] = i - 65 + 1

def f_alpha_value(s):
	# функция принимает слово в верхнем регистре и возвращает алфавитное значение слова 
    reslt = 0

    for letter in s:
        reslt += alpha_dict[letter]

    return reslt


def f_read_file(filename):
	# чтение из файла, принимает название файла, возвращет отсортированный список 
	strk_list = []

	with open(f'data/{filename}.txt', 'r') as in_file:
		names_list = in_file.read().split(',')

	# сортировка и удаление дополнительных "
	names_list.sort()
	#names_list = [elem[1:len(elem)-1] for elem in names_list]
	names_list = [elem.replace('"', '') for elem in names_list]

	return names_list


name = f_read_file('p022_names')

sum = 0
for i in range(len(name)):
	sum += f_alpha_value(name[i]) * (i+1)

print(sum)   #871198282






