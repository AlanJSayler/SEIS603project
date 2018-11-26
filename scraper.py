import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://www.eecs.mit.edu/people/faculty-advisors") as response:
    html = response.read()

authors = []
soup = BeautifulSoup(html, "html.parser")
for field_content in soup.find_all('span', {'class':'field-content card-title'}):
    authors.append(field_content.text.strip())

print(authors)

