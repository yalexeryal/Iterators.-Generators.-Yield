import json


class GetCountriesWiki:

    def __init__(self, file):
        with open(str(file)) as f:
            self.countries = json.load(f)
        self.start = -1
        self.end = len(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        name = self.countries[self.start]['name']['common']
        return f'{name} - https://en.wikipedia.org/wiki/{name.replace(" ", "_").replace(",", "_")};\n'
