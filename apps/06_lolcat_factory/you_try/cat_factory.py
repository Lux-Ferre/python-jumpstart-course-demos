import os
from apps import jumpstart

def get_folder():
    folder = "data"
    sub_path = "06_lolcat_factory/you_try"
    full_path = os.path.abspath(os.path.join(".", sub_path, folder))

    if not os.path.exists(full_path):
        os.mkdir(full_path)

    return full_path

def fetch_cats(folder_path):
    pass

def main():
    jumpstart.print_title("LOL CAT FACTORY")
    folder_path = get_folder()
    fetch_cats(folder_path)

if __name__ == '__main__':
    main()