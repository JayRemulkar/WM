# Scrape an online E-Commerce Site for Data

import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    phones = soup.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"})
    titles, prices, descriptions = list(),list(),list()

    for phone in phones:
        title = phone.find("a", {"class": "title"}).text.strip()
        price = phone.find("h4", {"class": "pull-right price"}).text.strip()
        description = phone.find("p", {"class": "description"}).text.strip()

        titles.append(title)
        prices.append(price)
        descriptions.append(description)

    df = pd.DataFrame({"Title": titles,"Price": prices,"Description": descriptions,})

    print(df)

if __name__ == "__main__":
    main()


   