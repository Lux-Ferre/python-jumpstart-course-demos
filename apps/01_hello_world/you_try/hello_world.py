def print_title():
    print('---------------------------')
    print('        HELLO WORLD')
    print('---------------------------')
    print()

def main():
    print_title()
    name_input = input('What is your name? ')
    print('Hello ' + name_input)

if __name__ == '__main__':
    main()