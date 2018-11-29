from scraper import scrape

def getFacultyAdvisors():
    return scrape("http://www.eecs.mit.edu/people/faculty-advisors", "span", "field-content card-title")

