import requests
from bs4 import BeautifulSoup

BookName = input()

BASE_URL = f'http://libgen.li/search.php?req=${BookName}&view=detailed&res=25'

source_code = requests.get(BASE_URL).text

soup = BeautifulSoup(source_code, 'lxml')

books = []

tbody = soup.find_all('tbody')

for each in tbody:
    try:
        temp = []
        book = dict()
        book["image"] = "libgen.li" + each.find('img')['src']
        for x in each.find_all('a'):
            temp.append(x.text)
        # print(temp, book)
        book["name"] = temp[1]
        tempString = ''
        for i in range(2, len(temp)):
            if temp[i] != 'Link':
                tempString += temp[i]
                tempString += ','
            else:
                break
        book['writer'] = tempString
        books.append(book)
    except:
        print("Helllop")

print(books)