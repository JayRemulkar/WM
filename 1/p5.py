# P5 Develop a focused crawler for local search.
"""https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=610644601173&hvpos=&hvnetw=g&hvrand=14641403356817447038&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300016&hvtargid=kwd-10573980&hydadcr=14453_2316415&gclid=Cj0KCQiA6fafBhC1ARIsAIJjL8msNusr-1Bj0TMb0GzAihcIELNDgqJZ81Z8IkUvqTLlhaxb-UpKsBUaAgUYEALw_wcB
https://scaleunlimited.com/about/focused-crawler
https://www.python.org/
https://www.cse.iitb.ac.in/~soumen/focus/
https://www.equitymaster.com/stockquotes/0-ADANI/list-of-adani-group-stocks
https://en.wikipedia.org/wiki/Focused_crawler"""

import requests
from bs4 import BeautifulSoup
from sys import *

def PageContains(url):      
    try:
        r = requests.get(url)               
        Contains = r.text
        r.close()    
        data = BeautifulSoup(Contains, "html.parser")
        return (data.get_text())
    
    except Exception as E:
        print(E)
        return ["Error : Unable to connect to the url"]

def Selector(data,target):
    flage = False
    
    for tar in target:
        for i in range(0,(len(data)+1)//2,1):
            if(tar.lower() == data[i].lower() or tar.lower() == data[(len(data)-1)-i].lower()):
                flage = True
                break
    
    return flage            

def FocusedCrawler(links,target):       
    data = dict()
    
    for link in links:
        linkdata = PageContains(link)
        bret = Selector(str(linkdata).split(),target)
        #print(bret,link)
        print(linkdata)
        if bret:
            data[link] = linkdata
    
    return data
        
def main():

    fd = open("p5test.txt","r")
    links = []
    target = ["crawler"]
    
    while True:
        line = fd.readline()
        if not line:
            break
        links.append(line)
    fd.close()
    
    ret = FocusedCrawler(links,target)
    sep = "-"*80
    
    icnt = 0
    for key in ret:
        icnt+=1
        print(sep+"\n"+"LINK : "+key+"\n"+sep+"\n"+"DATA : "+ret[key]+sep)
    print(icnt)

if __name__ == "__main__":
    main()