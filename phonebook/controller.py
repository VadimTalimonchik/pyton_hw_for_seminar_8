
from view import menu, show_contacts
from db_manager import open_file, get

def start():
    while True:
        choice = menu()
        if choice == 1:
            open_file()
        if choice == 3:
            pb = db_manager.get()
            show_contacts(pb)
        if choice == 8:
            print('До свидания!')
            break
        # match choice:
            # case 1:
            #     open_file()
            # case 2:
            #     pass
            # case 3:
            #     pass
            # case 4:
            #     pass
            # case 5:
            #     pass
            # case 6:
            #     pass
            # case 7:
            #     pass
            # case 8:
            #     print('До свидания!')
            #     break