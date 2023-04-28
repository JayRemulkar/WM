# P1 Scrap an online E-Commerse Site For Data.
# Rules to Follow 
# 1 Procedural Approch
# 2 less Memory Usage and proper connections closing 

from sys import exit
from bs4 import BeautifulSoup
import requests

def Helper(url):
    try:
        # get reqeust Makes a connection with the url.
        r = requests.get(url)               
        # text returns the content of the url/website
        Contains = r.text
        # terminates the connection
        r.close()    
    
    # if any Exception Occcurs it will print the Exception and end the program
    except Exception as E:
        print("Exception : ",E)
        exit(0)
    
    # Parsing the Contains
    data = BeautifulSoup(Contains, "html.parser")
    
    # Finding the parsed attributed in BeautifulSoup object. 
    links = data.find_all('div',attrs={'class':"a-expander-content a-expander-partial-collapse-content"})
    
    for i in links :
        print(i.text+" \n")
        
def main():
    url = 'https://www.amazon.in/Apple-iPhone-128GB-Product-RED/product-reviews/B0BDJVSDMY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    ret = Helper(url)

if __name__ == "__main__":
    main()