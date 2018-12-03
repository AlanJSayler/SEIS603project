#Alan
#Ade
#Saritha
from scraper import scrape
from json import dumps
from urllib import parse

faculty = scrape("http://www.eecs.mit.edu/people/faculty-advisors", "span", "field-content card-title")
goodInput = False
while not goodInput:
    goodInput = True
    try:
        mode = int(input("Welcome to the mit scraper app, press 1 to scrape article titles, or 2 to scrape abstracts: "))
    except:
        print("Cannot cast input to int, try again")
        goodInput = False
        continue
    if(mode == 1):
        arxivArgs = {"element":"p",
                "class":"title is-5 mathjax",
                "mode":"title"}
    elif(mode == 2):
        arxivArgs = {"element":"span",
                "class":"abstract-full has-text-grey-dark mathjax",
                "mode":"abstract"}
    else:
        print("sorry, that wasn't a 1 or 2")
        goodInput = False

with open('articles.json', 'w') as file:
    for advisor in faculty:
        mitArgs = {
            "query" : advisor,
            "searchtype" : "author",
            "abstracts" : "show"
        }
        for abstract in scrape("https://arxiv.org/search/?{}".format(parse.urlencode(mitArgs)),
                               arxivArgs.get("element",""),
                               arxivArgs.get("class","")):
            entry = {"author" : advisor,
                     arxivArgs.get("mode","") : abstract}
            print(entry)
            file.write(dumps(entry, indent = 4) + "\n",)



