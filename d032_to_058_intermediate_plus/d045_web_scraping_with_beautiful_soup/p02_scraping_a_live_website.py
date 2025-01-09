# Import required modules.
from bs4 import BeautifulSoup
import requests

# Scrape data from Hacker News. Save it to a variable and soup it.
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

# Separate out the titles with links included, and scores, per post.
# Find scores by checking subtexts for score elements, to weed out ads.
posts = soup.find_all(class_="titleline")
subtexts = soup.find_all(class_="subtext")
scores = []
for subtext in subtexts:
    if not subtext.find(class_="score"):
        scores.append(0)
    else:
        scores.append(subtext.find(class_="score").getText().split()[0])

# Create a dict of all posts from the front page. Title, link, score.
articles = []
for i in range(len(posts)):
    articles.append({
        "title" : posts[i].contents[0].getText(),
        "link" : posts[i].contents[0].get("href"),
        "score" : int(scores[i])
    })

# Iterate through the list of articles, saving the highest-voted one.
# At the end, print that article to the console.
max_title = ""
max_link = ""
max_score = 0
for i in articles:
    if i["score"] > max_score:
        max_title = i["title"]
        max_link = i["link"]
        max_score = i["score"]
print(f"{max_title} (+{max_score}) | {max_link}")