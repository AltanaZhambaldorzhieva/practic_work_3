import math

a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))

angle_a = int(math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))))
angle_b = int(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))))
angle_c = int(180 - angle_a - angle_b)

print(f"Угол A: {angle_a} градусов")
print(f"Угол B: {angle_b} градусов")
print(f"Угол C: {angle_c} градусов")
