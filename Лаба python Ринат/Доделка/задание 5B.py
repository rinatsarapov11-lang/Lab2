while True:
    x = int(input("Число 1: "))
    y = int(input("Число 2: "))
    i = input("Опеарация: ")
    if i == "+": print(x+y)
    elif i == "-": print(x-y)
    elif i == "*": print(x*y)
    elif i == "/": print(x/y if y !=0 else "Ошибка")
    if input("Ещё? ") == "нет": break