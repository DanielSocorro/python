import random


def run():
    random_number = random.randint(1, 100)
    choosen_number = int(input('choose a number between 1 to 100: '))
    while choosen_number != random_number:
        if choosen_number < random_number:
            print('Choose a higher number')
        else:
            print('Choose a lower number')
        choosen_number = int(input('enter another number: '))
    print('You Win !')


if __name__ == '__main__':
    run()