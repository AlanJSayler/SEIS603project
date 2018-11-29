from arxiv import getAbstracts
from mit import getFacultyAdvisors

faculty = getFacultyAdvisors()
abstracts = {}
for advisor in faculty:
    abstracts.update({advisor : getAbstracts(advisor, "author")})

print(abstracts)
