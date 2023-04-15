#a trial of bs4 from tech with tim tutorial: https://youtu.be/gRLHr664tXA
from wraps import *
from bs4 import BeautifulSoup as bs
import requests

def advanced_jobsearch_simplyhired():
    position = str(input("Position:"))
    location = str(input("Location:"))
    url = 'https://www.simplyhired.co.in/search?q={}&l={}'.format(position,location)
    results = requests.get(url)
    doc = bs(results.text,"html.parser")
    #print(doc.prettify())

    info = doc.find_all("div", class_="SerpJob-jobCard card")
    for i in range (len(info)):
        print(info[i].parent('span')[0].text)
        link_to_job = info[i].parent('a')[0]["href"]
        print(info[i].parent('a')[0].text)
        url_inside = 'https://www.simplyhired.co.in{}'.format(link_to_job)
        print(url_inside)
        results_internal = requests.get(url_inside)
        #print(url_inside)
        doc_internal = bs(results_internal.text,"html.parser")
        #print(doc_internal.prettify())
        qualifications = doc_internal.find_all("ul", class_="Chips")
        print(qualifications[0].text.split())

@findtime
def advanced_jobsearch_google():
    #position = str(input("Position:"))
    #location = str(input("Location:"))
    url = 'https://www.google.com/search?q=scrapping+internship+websites&oq=scrapping+internship+websites&aqs=edge..69i57j0i546l5j69i64.11080j0j1&sourceid=chrome&ie=UTF-8'
    results = requests.get(url)
    doc = bs(results.text,"html.parser")
    print(doc.prettify())
    #info = doc.find_all("div", class_="v7W49e")
    #rint(info)


if __name__ == '__main__':
    #advanced_jobsearch_simplyhired()
    advanced_jobsearch_google()