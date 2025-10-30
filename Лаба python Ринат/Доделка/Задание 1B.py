import random
secret_number = random.randint(1, 10)
print("Я загадал число от 1 до 10. Угадай его!")
while True:
    guess = int(input("Введи своё число: "))
    if guess == secret_number:
        print("Поздравляю! Ты угадал!")
        break
    elif guess < secret_number:
        print("Слишком мало! Попробуй больше.")
    else:
        print("Слишком много! Попробуй меньше.")