# Develop a basic crawler for the web search

import requests
from bs4 import BeautifulSoup

def main():
    
    url=("www.amazon.in")
    code=requests.get("https://"+url)
    plain=code.text
    soup=BeautifulSoup(plain,"html.parser")
    
    for link in soup.find_all('a'):
        print(link.get('href'))

if __name__ == "__main__":
    main()