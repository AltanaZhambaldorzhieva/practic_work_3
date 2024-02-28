whole_num = int(input('Введите число в диапазоне от 1 до 86400: '))
sec_day = 86400
hour = whole_num // 3600
minute = (whole_num % 3600) // 60
sec = (whole_num % 3600) % 60
print('Данное время: ', hour, 'часов', minute, 'минут', sec, 'секунд.')



