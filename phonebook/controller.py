
import db_manager
import view

def start():
    while True:
        choice = view.menu()
        if choice == 1:
            db_manager.open_file()
        if choice == 2:
            db_manager.save_file()
        if choice == 3:
            pb = db_manager.get()
            view.show_contacts(pb)
        if choice == 4:
            new = view.new_contact_input
            db_manager.add(new)
        if choice == 5:
            pass
        if choice == 6:
            find = view.find_contact()
            result = db_manager.find(find)
            view.show_contacts(result)
        if choice == 7:
            pass
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