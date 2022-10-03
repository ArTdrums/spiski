import random
spisok =[]# создаем путстой список
for i in range(10): #создаем цикл по 10 элементам
    spisok.append(random.randint(0,30)) # создаем список из случайных значений в диапозоне от 0 до 30
spisok_res = [x for x in spisok if x > 5 ] # запустил генератор списков
print(spisok_res)
print(sum(spisok_res) / len(spisok_res)) # выводим средее арифм. фун лен- длина списка, сум - сумма эл.

'''import random
spisok =[]
count = 0
for i in range(10):
    spisok.append(random.randint(0,30)) # создаем список из случайных значений в диапозоне от 0 до 30
spisok_res = [x for x in spisok if x > 5 ] # запустил генератор списков
for i in spisok_res:
     count +=1
print(spisok_res)
print(sum(spisok_res) / count)
'''