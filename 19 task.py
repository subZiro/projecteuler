#!/usr/bin/python
# -*- coding: utf-8 -*-



"""
_____________________________________
Дана следующая информация (однако, вы можете проверить ее самостоятельно):
1 января 1900 года - понедельник.
В апреле, июне, сентябре и ноябре 30 дней.
В феврале 28 дней, в високосный год - 29.
В остальных месяцах по 31 дню.
Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00) 
является високосным в том и только том случае, если делится на 400.

Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?
"""


import datetime

def f_count_weekend(day_start, day_finish):
	# функця принимает начальную и конечную дату периода времени 
	# возвращает список с датами в когда воскресенье выпадало на первое число месяца 
	weekday_list = []

	while day_start <= day_finish:   
		# если текущяя дата первое число и этот день воскресенье, то добавляем дату в список
		if  day_start.day == 1 and day_start.isoweekday() == 7:  
			weekday_list.append(day0)

		day_start += datetime.timedelta(1)   #увеличивает счетчик на 1 день 

	return weekday_list



day0 = datetime.date(1901, 1, 1)  # стартовая дата 
dayX = datetime.date(2000, 12, 31)   # финишная дата

print(len(f_count_weekend(day0, dayX)))      # 171 

