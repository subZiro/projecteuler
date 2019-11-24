#!/usr/bin/python
# -*- coding: utf-8 -*-




"""
____________________________________________________
Если записать числа от 1 до 5 английскими словами 
(one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?

Примечание: Не считайте пробелы и дефисы. Например, 
число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. 
Использование "and" при записи чисел соответствует правилам британского английского."""


nums={1:'one', 2:'two', 
	3:'three', 4:'four',
	5:'five', 6:'six',
    7:'seven', 8:'eight',
    9:'nine', 10:'ten',
    11:'eleven', 12:'twelve',
    13:'thirteen', 15:'fifteen',
    18:'eighteen', 20:'twenty',
    30:'thirty', 40:'forty',
    50:'fifty', 60:'sixty',
    70:'seventy', 80:'eighty',
    90:'ninety',
    }



def gen_num(user_n, nums_dict):
	# функция принимает число, которое нужно преобразовать в строковон значение этого числа
	# и словарь ключ-число, значение-строковое описание числа
    tmp = ''
    n_to_str = str(user_n)

    if nums_dict.get(user_n, False):
        return nums_dict[user_n]
    elif user_n < 20:
        return nums_dict[int(n_to_str[1])] + 'teen'
    elif user_n < 100:
        tmp = user_n - int(n_to_str[1])
        return nums_dict[tmp] + nums_dict[int(n_to_str[1])]
    elif user_n < 1000:
        if n_to_str[1:3] == '00':
            return nums_dict[int(n_to_str[0])] + 'hundred'
        else:
            return nums_dict[int(n_to_str[0])] + 'hundredand' + gen_num(int(n_to_str[1:3]),nums_dict)
    elif user_n == 1000:
        return 'onethousand'


num_str = ''
sum_lett = 0

for i in range(1, 1001):
	num_str = gen_num(i, nums)
	#print(num_str)
	sum_lett += len(num_str)

print(sum_lett)    # 21124



