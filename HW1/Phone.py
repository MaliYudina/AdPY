"""
Class definition for a Contact
"""


class Contact:
    def __init__(self, name, surname, number, favourite=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.favourite = favourite
        self.tuple = args
        self.dict = kwargs

    def __str__(self):
        print('''
Имя: {0}
Фамилия: {1}
Телефон: {2}
В избранных: {3}
Дополнительная информация:'''.format(str(self.name), str(self.surname), str(self.number), str(self.favourite)))
        for key, value in self.dict.items():
            print('{0} : {1}'.format(key, value))


"""
Class definition for the PhoneBook
"""


class PhoneBook:
    def __init__(self, title):
        self.title = title
        self.contacts = []

    def add_contact(self, person):
        self.contacts.append(person)

    def all_contacts(self):
        for item in self.contacts:
            item.__str__()

    def delete(self, phone_number):
        n = int()
        for item in self.contacts:
            if item.number == phone_number:
                self.contacts.remove(item)
                n += 1
                break
            else:
                pass
        if n == 0:
            print('Данный контакт не найден.')

    def fav_search(self):
        favourite_list = {}
        for item in self.contacts:
            if item.favourite:
                favourite_list[item.name] = item.favourite
        print('Список избранных:')
        for key, value in favourite_list.items():
            print('{0}'.format(key, value))

    def name_search(self, name, surname):
        n = int()
        for item in self.contacts:
            if name == item.name and surname == item.surname:
                item.__str__()
                n += 1
                break
            else:
                pass
        if n == 0:
            print('Такого контакта не существует!')


katie = Contact('Katie', 'Smith', '+65670880', True, email='ks@bk.ru')
james = Contact('James', 'Trump', '+7865971', False, email='65fd@gmail.com')
jack = Contact('Jack', 'Punisher', '+5452564', True, email='765@g.si')
helen = Contact('Helen', 'Peterson', '555', False, home_number='+8953568798', telegram='@hp87er')

all_list = [katie, james, jack, helen]

book = PhoneBook(title='My Phone Book')
for item in all_list:
    book.add_contact(item)

print('----- Список всех контактов -----')
book.all_contacts()

book.delete('555')

print('----- Обновленный список контактов (после удаления номера) -----')
book.all_contacts()

print('----- Поиск избранных контактов -----')
book.fav_search()

print('----- Поиск по имени и фамилии -----')
book.name_search('James', 'Trump')
