from random import randint
from apps import jumpstart

def main():
    jumpstart.print_title('NUMBER GUESS')
    random_number = randint(0, 100)
    player_number = int(input('What is your guess? '))
    while player_number != random_number:
        if player_number < random_number:
            print("Sorry, %d is less than the number. Try again." % player_number)
            player_number = int(input('What is your guess? '))
        else:
            print("Sorry, %d is more than the number. Try again." % player_number)
            player_number = int(input('What is your guess? '))
    print('Well done! The number was %d' % player_number)


if __name__ == '__main__':
    main()