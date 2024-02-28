att = int(input("Введите число попыток передач: "))
comp = int(input("Введите число завершенных передач: "))
yds = int(input("Введите количество ярдов: "))
td = int(input("Введите количество пасов приземления: "))
inter = int(input("Введите количество перехватов: "))

a = ((comp/att - 0.3) * 5)
b = ((yds/att - 3) * 0.25)
c = (td/att * 20)
d = 2.375 - ((inter/att * 25))

a = 2.375 if a > 2.375 else a
b = 2.375 if b > 2.375 else b
c = 2.375 if c > 2.375 else c
d = 2.375 if d > 2.375 else d

passer_rating = ((a + b + c + d) / 6) * 100
print(f"Квотербек рейтинг игрока: {passer_rating}")
