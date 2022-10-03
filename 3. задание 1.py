pervoe_4islo = int(input("Введите первое число: "))
vtoroe_4islo = int(input("Введите второе число: "))
tretie_4islo = int(input("Введите третье число: "))
if pervoe_4islo > vtoroe_4islo and pervoe_4islo > tretie_4islo:
    print("самое большое число - это первое")
elif vtoroe_4islo > pervoe_4islo and vtoroe_4islo > tretie_4islo:
    print("самое большое число - это второе")
else:
    print("самое большое число - это третье")

# определяем меньшее из трех введенных пользователем чисел
if pervoe_4islo < vtoroe_4islo and pervoe_4islo < tretie_4islo:
    print("самое маленькое число - это первое")
elif vtoroe_4islo < pervoe_4islo and vtoroe_4islo < tretie_4islo:
    print("самое маленькое число - это второе")
else:
    print("самое маленькое число - это третье")