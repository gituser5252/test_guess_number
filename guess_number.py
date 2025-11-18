from random import randint
number = int(input())
number_random = randint(1, 100)
while True:
    if number > number_random:
        print('Ваше число больше того, что загадано')
    elif number < number_random:
        print('Ваше число меньше того, что загадано')
    else:
        print('Отличная интуиция! Вы угадали число :)')
        break
    number = int(input('Попробуйте снова - '))
