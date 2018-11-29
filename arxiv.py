from urllib import parse
from scraper import scrape

BASE_URL = 'https://arxiv.org/search/?'

def getAbstracts(query, searchtype):
    args = {
        "query" : query,
        "searchtype" : searchtype,
        "abstracts" : "show"
    }
    return scrape("{}{}".format(BASE_URL, parse.urlencode(args)),'span',"abstract-full has-text-grey-dark mathjax")