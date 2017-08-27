import random
import urllib.request

def downloadImagefromNet(url):
    number = random.randrange(0, 100)   #generates a random numner between 0 to 100
    imageName = str(number) + '.jpg'
    urllib.request.urlretrieve(url, imageName)

downloadImagefromNet('http://gratisography.com/pictures/425_1.jpg')