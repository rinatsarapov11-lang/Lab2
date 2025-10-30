a = int(input("Введите число"))
if a<2:
    print("нет")
else:
    for i in range(2, int(a**0.5) + 1):
        if a % i  == 0:
            print("нет")
            break
    else:
        print("да")