#Alan
#Ade
#Saritha
from arxiv import getAbstracts
from mit import getFacultyAdvisors
from json import dumps

faculty = getFacultyAdvisors()
articles = []
for advisor in faculty:
    for abstract in getAbstracts(advisor,"author"):
        entry = {"author" : advisor,
                 "abstract" : abstract}
        articles.append(entry)

print(articles)
with open ('articles.json', 'w') as file:
    file.write(dumps(articles))
