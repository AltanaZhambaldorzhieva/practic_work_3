x, y, n = map(int, input('Введите через пробел стоимость латте в руб/коп и количество заказов: ').split())
income = (x * 100 + y) * n
r = income // 100
k = income % 100
print(f"{r} руб {k} копеек")
