import db_manager
import view

pb = db_manager.PhoneBook()

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                pb.open_file()
            case 2:
                pb.save_file()
            case 3:
                book = pb.get()
                view.show_contacts(book)
            case 4:
                new = view.new_contact_input()
                pb.add(new)
            case 5:
                book = pb.get()
                view.show_contacts(book)
                ind = view.input_id()
                contact = view.new_contact_input()
                pb.change_contact(ind, contact)
            case 6:
                find = view.find_contact()
                result = pb.find(find)
                view.show_contacts(result)
            case 7:
                book = pb.get()
                view.show_contacts(book)
                ind = view.input_id()
                name = pb.get_name(ind)
                if view.confirm('\nУдалить данные',name):
                    pb.delete_contact(ind)
            case 8:
                if pb.check_changes():
                    if view.confirm_changes():
                        pb.save_file()
                print('\nДо свидания!')
                break

