#Alan
#Ade
#Saritha
from urllib import request
from bs4 import BeautifulSoup


#return a list of strings corresponding to the type and class in a document
#given by url
def scrape(url,getType,getClass):
    with request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for field_content in soup.findAll(getType, {'class' : getClass}):
        results.append(field_content.text.strip())
    return results














