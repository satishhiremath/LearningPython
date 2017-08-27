import requests
from bs4 import BeautifulSoup

def weCrawler(max_pages):
    page = 1
    while(page <= max_pages):
        url = 'https://www.listchallenges.com/lists/books/trending/' + str(page)
        print(url)
        urlData = requests.get(url)
        textData =  urlData.text
        soup = BeautifulSoup(textData)

        for itemName in soup.findAll('div', {'class' : 'list-name'}): ##findAll(<htmlElement>, {<attribute>: <value>}
            #<div class="list-name">BBC's The Big Read - Best Loved Novels of All Time</div>
            #prints all books name in pages
            print(itemName.string)
        page += 1


weCrawler(3)