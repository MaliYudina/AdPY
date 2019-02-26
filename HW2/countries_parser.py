import json

SOURCE_FILE = 'countries.json'
FILE_TO_WRITE = 'countries_link.txt'

"""
Написать класс итератора, который по каждой стране из файла countries.json
ищет страницу из википедии.
Записывает в файл пару: страна – ссылка.
"""


class WikipediaData:
    def __init__(self, FILE_TO_WRITE, output):
        self.countries = json.load(open(FILE_TO_WRITE))
        self.ind = -1
        countries = json.load(open(SOURCE_FILE))
        self.max_range = len(countries)
        self.out = open(output, 'w', encoding='utf8')

    def __iter__(self):
        return self

    def __next__(self):
        self.ind += 1
        while self.ind >= self.max_range:
            self.out.close()
            raise StopIteration
        return self.countries[self.ind]['name']['official']

    def write_country(self, country):
        url = f'https://en.wikipedia.org/wiki/{country}'
        self.out.write(f'{country} - {url}\n')


result = WikipediaData(SOURCE_FILE, FILE_TO_WRITE)

for country in result:
    result.write_country(country)
