number = input("Введите число")
long=len(number)
new_number=""
for i in range(long-1, -1, -1):
    new_number+=number[i]
print(new_number)
