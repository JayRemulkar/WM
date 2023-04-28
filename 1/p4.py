# P4 Develop a basic crawler for the web search for user defined keywords.

import requests
from bs4 import BeautifulSoup
import socket
import validators

def is_connected():     # it checks if internet is connected
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False

def LinkValidator(link):        # checks if link is valid
    valid = validators.url(link)
    if valid == True:
        return True
    else:
        return False

def Connection(url):        # connects to the url and sends back the data
    try:
        r = requests.get(url)               
        Contains = r.text
        r.close()    
        data = BeautifulSoup(Contains, "html.parser")
        return data.get_text()
    
    except Exception as E:
        return "Error : Unable to connect to the url"

def Crawler(Arr):       # make a dict and returns it
    result = is_connected()

    data = dict()
    
    if result:
        if type(Arr) == list:
            for link in Arr:
                result = LinkValidator(link)
                if result:
                    linkdata = Connection(link)
                    data[link] = linkdata

                else:
                    data[link] = "Error : The Given Link is not Valid!"
    
    return data
        
def main():
    Dataset = Crawler(["https://en.wikipedia.org/wiki/India","https://en.wikipedia.org/wiki/Dennis_Ritchie","https://github.com/","https://en.wikipedia.org/wiki/One_Piece"])
    sep = "-"*80

    for key in Dataset:
        print(sep)
        print("URL : ",key)
        print("DATA : ",Dataset[key])

    print(sep)

if __name__ == "__main__":
    main()