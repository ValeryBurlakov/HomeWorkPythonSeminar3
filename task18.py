import random
n = int(input("Введите размер массива: "))
l = []
# l = [(i + 1) for i in range(n)]
for i in range(n):
    l.append(random.randint(1, 9))
print(l)
x = int(input("Введите число: "))
print("ищем число, либо ближайшее по величине")
result = l[0]
for i in l:
    if abs(i - x) < abs(result - x):
        result = i
if result == x:
    print(f"ваше число {x} находится в массиве")
else:
    print(f"Ближайщее число к {x} это - {result}")