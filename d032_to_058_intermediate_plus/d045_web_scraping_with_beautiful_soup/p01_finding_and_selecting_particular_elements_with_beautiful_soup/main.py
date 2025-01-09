from bs4 import BeautifulSoup

# Open the HTML file and save the contents to a variable.
with open('index.html') as f:
    contents = f.read()

# Run the contents of the HTML file through BS4 using the HTML parser.
soup = BeautifulSoup(contents, "html.parser")

# Finding all anchor tags in the HTML file and iterating through.
# You can print the full thing, just the text, or the link itself.
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
#    print(tag)
#    print(tag.getText())
    print(tag.get("href"))

# Find a specific element by its name.
heading = soup.find(name="h1", id="name")
print(heading)

# Find a specific element by its class. Note the underscore.
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# Find a specfic element by its selector. Look for an anchor inside a paragraph.
company_url = soup.select_one(selector="p a")
print(company_url)

# Create a list of everything matching the given criteria.
headings = soup.select(".heading")
print(headings)