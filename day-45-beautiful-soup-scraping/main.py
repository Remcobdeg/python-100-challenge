
from bs4 import BeautifulSoup
import os

os.chdir(os.path.dirname(__file__))

with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser") # Or "lxml"
print(soup.title) # <title>My Awesome Website</title>
print(soup.title.name) # title
print(soup.title.string) # My Awesome Website

print(soup.prettify()) # Pretty print the HTML

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading) 