sum = 0
count = 0
x = 1
while x != 0:
    x = int(input("Введите число : "))
    if x != 0:
        sum += x
        count += 1
if count > 0:
    print(sum / count)
