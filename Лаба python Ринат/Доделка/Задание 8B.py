n = input("Введите число: ")
min_digit = n[0]
for digit in n:
    if digit < min_digit:
        min_digit = digit
print(min_digit)