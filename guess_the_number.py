# Угадай число
# Рандомное число, которые нужно угадать за 7 попыток
import random

number = random.randint(1, 20) # Рандом 1-20
TRIES_COUNT = 7 # Константа, начальное количество попыток

print('!', number) # Загаданное число

for i in range(TRIES_COUNT):
    user = int(input())
    
    if user > number:
        print('Загаданое число меньше. Осталось попыток:', TRIES_COUNT - 1 - i)
    if user < number:
        print('Загаданое число больше. Осталось попыток:', TRIES_COUNT - 1 - i)
    if user == number:
        print('Угадал - ', number)
        break
else:
    print('Ты проиграл, попытки закончились')
