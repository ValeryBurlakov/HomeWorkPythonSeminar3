import random

lst = []
n = int(input("Введите размер массива: ")) # ручной ввод по условию
# n = random.randint(5, 10) # рандомный ввод
for i in range(n):
    lst.append(i + 1) # заполнение по условию
    # lst.append(random.randint(1, 9)) # рандомное заполнение
print(lst)
# x = random. randint(1, 9) # рандомный x
x = int(input("Введите искомое число x : ")) # ручной ввод
print(f"проверяем сколько раз в массиве встречается число x = {x}.")

count = 0
for i in lst:
    if i == x:
        count += 1

if count > 0:
    print(f"число {x} встречается {count} раз(раза)")
elif count == 0:
    print(f"число {x} не найдено")