from urllib import request
from bs4 import BeautifulSoup


#Scrapes the requested url and returns a list of all text found within the specified
#span or div class
def scrape(url,getType,getClass):
    with request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for field_content in soup.findAll(getType, {'class' : getClass}):
        results.append(field_content.text.strip())
    return results










