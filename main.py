from library.get_wiki import GetCountriesWiki as Gcw
from library.hash_generator import hash_generator as hg

if __name__ == '__main__':
    with open('countries_links.txt', 'w', encoding='utf-8') as f:
        for country in Gcw('countries.json'):
            f.write(country)

    for lh in hg('countries_links.txt'):
        print(lh)
