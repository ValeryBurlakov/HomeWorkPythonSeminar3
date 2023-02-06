import random
# n = int(input("Введите размер массива: ")) # ручной ввод по условию
n = int(random.randint(5, 10)) # рандомный ввод
l = []
l = [(i + 1) for i in range(n)] # заполнение по условию

print(l)
print("Будем искать число, либо ближайшее по величине:")
x = random. randint(-10, 15) # рандомное число
# x = int(input("Введите число: ")) # ручной ввод числа

result = l[0]
for i in l:
    if abs(i - x) < abs(result - x):
        result = i
if result == x:
    print(f"ваше число {x} находится в массиве")
    
else:
    print(f"Ближайщее число к {x} это: {result}")

if x > 1 and x < n:
    print(f"но ближайшие к нему: {x - 1} и {x + 1}")
elif x == 1:
    print(f"Но ближайшее: {x + 1}")
elif x == n:
    print(f"Но ближайшее: {n - 1}")