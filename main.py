import random


def game_decorator(func):
    def wrapper():
        number = random.randint(1, 10)
        attemps=10
        print('Привет! Угадай число от 1 до 10')
        while attemps > 0:
            guess = int(input('Введите число:  '))
            if guess == number:
                print('Вы угадали')
                break
            elif guess < number:
                print('Загадонное число больше')
            else:
                print('Загадонное число меньше')
            attemps -= 1
        print(f'Количество попыток: {attemps}')

    return wrapper

@game_decorator
def play_game():
    pass
play_game()