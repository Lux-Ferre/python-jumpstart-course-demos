from apps import jumpstart
from datetime import datetime
from os import path
from dateutil import parser

def load_data():
    filename = path.abspath('./04_journal/you_try/data/journal.jrl')
    journal_data=[]
    if path.exists(filename):
        raw_data = open(filename, 'r')
        for line in raw_data:
            line_data = line.split(',')
            date_data = parser.parse(line_data[1]).date()
            entry_data = (line_data[0], date_data)
            journal_data.append(entry_data)
        raw_data.close()
    return journal_data

def save_data(entries):
    filename = path.abspath('./04_journal/you_try/data/journal.jrl')
    raw_data = open(filename, 'w+')
    for e in entries:
        save_line = '{},{}'.format(e[0], e[1])
        raw_data.write(save_line + '\n')
    raw_data.close()

def program_loop():
    entries = load_data()
    print('What do you want to do?')
    menu_input = input('[L]ist, [A]dd, or E[x]it?').lower()

    while menu_input != 'x':
        if menu_input == 'l':
            show_list(entries)
        elif menu_input == 'a':
            new_entry(entries)
        else:
            print('Sorry. "{}" was an invalid command. Try again.'.format(menu_input))
        menu_input = input('[L]ist, [A]dd, or E[x]it?').lower()
    print('Saving entries to file.')
    save_data(entries)
    print('Save successful.')

def show_list(entries):
    for e in entries:
        formatted_date = e[1].strftime("%d/%m/%y")
        print('{}: {}'.format(formatted_date, e[0]))

def new_entry(entries):
    print('Enter your journal entry: ')
    entry_data = input()
    today = datetime.today().date()
    entries.append((entry_data, today))

def main():
    jumpstart.print_title('JOURNAL APP')
    program_loop()

if __name__ == '__main__':
    main()