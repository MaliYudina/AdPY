from pprint import pprint
import csv
import re

SOURCE_FILE = 'phonebook_raw.csv'
PHONE_REGEX = '(\+7|8)(\s?)(\(?)(' \
              '[0-9]{3})(\)?)(\s?)(\-?)(' \
              '[0-9]{3})(\-?)([0-9]{2})(\-?)([0-9]{2})(\s?)(\(?)([а-яё]*)(\.?)' \
              '(\s?)([0-9]*)(\)?)'

with open(SOURCE_FILE, encoding='UTF-8') as f:
    line = csv.reader(f, delimiter=',')
    contacts_list = list(line)


for contact in contacts_list:
    order_1 = contact[0].split(' ')
    if len(order_1) == 3:
        contact[0] = order_1[0]
        contact[1] = order_1[1]
        contact[2] = order_1[2]
    elif len(order_1) == 2:
        contact[0] = order_1[0]
        contact[1] = order_1[1]
    else:
        pass
    order_2 = contact[1].split(' ')
    if len(order_2) == 2:
        contact[1] = order_2[0]
        contact[2] = order_2[1]
    else:
        pass

    normalized_phone = re.sub(PHONE_REGEX, r'+7(\4)\8-\10-\12\13\15\16\18', contact[5])
    contact[5] = normalized_phone


contacts_dict = {}
for contact in contacts_list:
    if contact[0] not in contacts_dict.keys():
        contacts_dict[contact[0]] = contact[1:]


normalized_contact_list = []
for key, value in contacts_dict.items():
    i_contact = [key]
    for i in value:
        i_contact.append(i)
    normalized_contact_list.append(i_contact)

pprint(normalized_contact_list)

with open('normalized_phonebook.csv', 'w', encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(normalized_contact_list)
