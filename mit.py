#Alan
#Ade
#Saritha
from scraper import scrape

#return faculty advisors from MIT eecs.
def getFacultyAdvisors():
    return scrape("http://www.eecs.mit.edu/people/faculty-advisors", "span", "field-content card-title")

