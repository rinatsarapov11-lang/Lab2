
a = int(input("Введите число: "))
n = int(input("Введите степень: "))

result = 1
for i in range(n):
    result *= a
print(f"{a} в степени {n} = {result}")