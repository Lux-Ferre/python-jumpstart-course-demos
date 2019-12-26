from apps import jumpstart
from datetime import date

def main():
    jumpstart.print_title('BIRTHDAY APP')
    today = date.today()
    birthday = get_data()

    print('So you were born on {}?'.format(birthday))

    current_year = date(today.year, birthday.month, birthday.day)
    time_delta = current_year - today
    days_to_birthday = time_delta.days

    if days_to_birthday < 0:
        print('It has been {} days since your birthday.'.format(-days_to_birthday))
    elif days_to_birthday > 0:
        print('It is {} days until your birthday.'.format(days_to_birthday))
    else:
        print('Happy birthday!')

def get_data():
    birth_year = int(input('What year were you born in? [YYYY] '))
    birth_month = int(input('What month were you born in? [MM] '))
    birth_day = int(input('What day were you born on? [DD] '))
    birthday = date(birth_year, birth_month, birth_day)

    return birthday

if __name__ == '__main__':
    main()