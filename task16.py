import random

lst = []
n = int(input("Введите размер массива: "))

for i in range(n):
    lst.append(random.randint(1, 9))
print(lst)
x = random. randint(1, 9)
# x = int(input("Введите искомое число x : "))
print(f"проверяем сколько раз в массиве встречается число x = {x}.")

count = 0
for i in lst:
    if i == x:
        count += 1

if count == 2 or count == 3 or count == 4:
    print(f"{x} встречается {count} раза")
elif count == 1 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9:
    print(f"{x} встречается {count} раз")
elif count == 0:
    print(f"число {x} не найдено")