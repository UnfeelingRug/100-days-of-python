# Import required modules.
from bs4 import BeautifulSoup
import requests

# Scrape data from the Top 100 Movies list. Save it to a variable and soup it.
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
top100 = response.text
soup = BeautifulSoup(top100, "html.parser")

# Pick out all movie titles from the h2 headings - remove "How We Chose."
titles = soup.find_all(name="h2")
titles.pop(0)

# Iterate backwards through the list, save them all to a text file.
with open("movies.txt", mode="w") as w:
    for i in range(len(titles)):
        title = titles[-i-1].getText()
        w.write(f"{title}\n")