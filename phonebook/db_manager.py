phone_book = []
path = 'phone_db.txt'

def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_contact = {}
            new_contact['name'] = new[0]
            new_contact['phone'] = new[1]
            new_contact['comment'] = new[2]
            phone_book.append(new_contact)


def save_file():
    global phone_book
    global path
    data = []
    for contact in phone_book:
        data.append(new = ';'.join(contact.values()))
        data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get():
    global phone_book
    return phone_book


def add(new_contact: dict):
    global phone_book
    phone_book.append(new_contact)


def find(find_option: str):
    global phone_book
    all_find = []
    for contact in phone_book:
        for element in contact.values():
            if find_option in element:
                all_find.append(contact)
    return all_find
    
