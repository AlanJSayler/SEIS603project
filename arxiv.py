#Alan
#Ade
#Saritha
from urllib import parse
from scraper import scrape

BASE_URL = 'https://arxiv.org/search/?'

#get abstracts from arxiv based on a query type and data
#in this project, we are only finding by author, but the code
#could be reused to find based on any query.
def getAbstracts(query, searchtype):
    args = {
        "query" : query,
        "searchtype" : searchtype,
        "abstracts" : "show"
    }
    return scrape("{}{}".format(BASE_URL, parse.urlencode(args)), 'span', "abstract-full has-text-grey-dark mathjax")