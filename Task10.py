#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монеток "))
count = 0
import random
for i in range(n):
    coin = random.randint(0,1)
    print(coin, end=' ')
    if coin ==1:
        count +=1
if count>n/2:
    count = n-count
else:
    count = count
print(f"минимальное количество монет, которые нужно перевернуть = {count}")





# n = int(input())
# k = 0
# import random
# for i in range(n):
#     v = random.randint(0,1)
#     if v == 1:
#         k += 1
# print(k if k<n/2 else n-k)

