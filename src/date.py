from bs4 import BeautifulSoup
import requests
def main():
    url='https://english.hamropatro.com/'
    site=requests.get(url)
    soup=BeautifulSoup(site.content,'html.parser',from_encoding="iso-8859-1")


    date=soup.select("div.date span.nep")
    event=soup.select("div.events a.event")

    for i in date:
        print(i.text)

    for i in event:
        print(i.text)





