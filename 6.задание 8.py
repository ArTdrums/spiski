'''
Написать программу, определяющую является ли введенный номер билета - "счастливым".
Билет называют «счастливым», если в его номере сумма первых трех цифр равна сумме последних трех.
Номер билета может быть от 000000 до 999999.
'''
a = input() # создаем переменную для ввода строки пользователем
b = list(a) # переводим сроку в список
for i in range(len(b)):# преобразуем список из строк в список из целых чисел
    b[i] = int(b[i])#
print(b)# выводим получившийся список
if sum(b[0:3]) == sum(b[3:6]):# сравниваем значение суммы элементов
    print('позравляем, вы выйграли счастоивый билет')# если условие выполняется выводим
else:#
    print("ваш билет не счастливый")# в противном случае выводим