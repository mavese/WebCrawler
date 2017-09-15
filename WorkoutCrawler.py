from bs4 import BeautifulSoup
import urllib
import requests
import re

def getLinks (startUrl):
    G = {startUrl: []}
    soup = BeautifulSoup(urllib.urlopen(startUrl).read(), 'lxml')
    links = soup.find_all('a', href=re.compile('^https://shop.workoutempire.com'))
    for link in links:
        G[startUrl].append(link.get('href'))
    return G

def getNames(url):
    soup = BeautifulSoup(urllib.urlopen(url).read(), 'lxml')
    nameList = [a for a in soup.find_all('label', {'class' : 'y-label yotpo-user-name yotpo-font-bold pull-left'})]
    return nameList

if __name__ == '__main__':
    startUrl = "https://shop.workoutempire.com/collections/womens-tights/products/i16w-aop-tights-obsidian"
    # print getNames(startUrl)
    soup = BeautifulSoup(urllib.urlopen(startUrl).read(), 'lxml')
    print soup.find_all('label')