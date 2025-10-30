b = 1000
while b > 0:
    print(f"Баланс: {b} руб")
    take = int(input("Сколько снять: "))
    if take <= b:
        b -= take
    else:
        print("Недостаточно Средств")
print("Деньги закончились")