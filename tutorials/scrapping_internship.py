from fastapi import FastAPI, Path,Query
import requests
from bs4 import BeautifulSoup as bs
app = FastAPI()

@app.get("/get-intern/{position}/{location}")
def jobsearch_simplyhired(position:str,location:str):
    intern_json = {}
    intern_list = []
    #position = str(input("Position:"))
    #location = str(input("Location:"))
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
        
        intern_list.append({"name":info[i].parent('span')[0].text,"link":info[i].parent('a')[0].text,'qualifications':qualifications[0].text.split()})
        intern_json["internships"] = intern_list
    return intern_json
        
        