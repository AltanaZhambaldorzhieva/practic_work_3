x, y = map(int, input('Enter numbers: ').split())
result = int(x % y == 0) or int(y % x == 0)
print(result)
