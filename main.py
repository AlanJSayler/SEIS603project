#Alan
#Ade
#Saritha
from scraper import scrape
from json import dumps
from urllib import parse

faculty = scrape("http://www.eecs.mit.edu/people/faculty-advisors", "span", "field-content card-title")
with open('articles.json', 'w') as file:
    for advisor in faculty:
        args = {
            "query" : advisor,
            "searchtype" : "author",
            "abstracts" : "show"
        }
        for abstract in scrape("https://arxiv.org/search/?{}".format(parse.urlencode(args)),
                               "span",
                               "abstract-full has-text-grey-dark mathjax"):
            entry = {"author" : advisor,
                     "abstract" : abstract}
            print(entry)
            file.write(dumps(entry) + "\n")



