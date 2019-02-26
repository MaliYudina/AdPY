import hashlib
from HW2.countries_parser import FILE_TO_WRITE


"""
Написать генератор, который принимает путь к файлу. 
При каждой итерации возвращает md5 хеш каждой строки файла.
"""


def hash_encode(link):
    return hashlib.md5(link.encode('utf-8')).hexdigest()


def hash_data(path):
    with open(path, 'r', encoding='utf8', ) as f:
        for line in f:
            yield hash_encode(line)


for i in hash_data(FILE_TO_WRITE):
    print(i)
