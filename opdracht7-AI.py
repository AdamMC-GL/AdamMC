import random


def Guess_Number():
    randomGetal = random.randint(0, 10)
    guess = None

    while guess != str(randomGetal):
        guess = input('Raad het getal tussen 1 en 10: ')
        if guess == str(randomGetal):
            print('You guessed it!')
            break
        print('Guess again')


Guess_Number()
