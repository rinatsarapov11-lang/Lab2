a = int(input("Первое число: "))
b = int(input("второе число: "))
while b != 0 :
    a, b = b, a % b
print("Нод=", a)