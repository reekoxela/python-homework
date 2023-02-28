class PhoneBook:
    phone_book: list
    old_phone_book: list

    def __init__(self, path: str = 'phone_db.txt'):
        self.path = path
        self.phone_book = []
        self.old_phone_book = []

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {}
                new_contact['name'] = new[0]
                new_contact['phone'] = new[1]
                new_contact['comment'] = new[2]
                self.phone_book.append(new_contact)
        self.old_phone_book = self.phone_book[:]
        print('\nТелефонная книга загружена!\n')

    def save_file(self):
        data = []
        for contact in self.phone_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        print('\nДанные сохранены!\n')
        self.old_phone_book = self.phone_book[:]

    def get(self):
        return self.phone_book

    def add(self, new_contact: dict):
        self.phone_book.append(new_contact)
        print(f'\nКонтакт {new_contact.get("name")} записан!\n')

    def find(self, find_option: str) -> list:
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_option.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def change_contact(self, ind: int, contact: dict):
        self.phone_book.pop(ind - 1)
        self.phone_book.insert(ind - 1, contact)

    def delete_contact(self, ind: int):
        contact = self.phone_book.pop(ind - 1)
        print(f'Контакт {contact.get("name")} удален!')

    def get_name(self, ind: int):
        return self.phone_book[ind - 1].get('name')

    def check_changes(self):
        if self.phone_book != self.old_phone_book:
            return True
        return False