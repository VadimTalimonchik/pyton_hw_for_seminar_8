

def menu():
    print('''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. удалить контакт
    8. Выход''')

    choice = int(input('Выберите пункт меню: '))
    return choice


def show_contacts(pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста или файл не открыт!')
    else:
        for i, contact in enumerate(pb):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')