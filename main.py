import requests
from bs4 import BeautifulSoup

class Books():
    def __init__(self, bookName):
        self.__bookName = bookName
        self.__request = f'http://libgen.li/search.php?req=${self.__bookName}&view=detailed&res=25'
        respond = requests.get(self.__request).text
        self.__soup = BeautifulSoup(respond, 'lxml')

    def getBooks(self):
        books = []
        tbody = self.__soup.find_all('tbody')
        for each in tbody:
            try:
                temp = []
                book = dict()
                book["image"] = "libgen.li" + each.find('img')['src']
                for x in each.find_all('a'):
                    temp.append(x.text)
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
                continue
        return books

book = input("Enter The Book Name >>> ")
bookObject = Books(book)
print(bookObject.getBooks())