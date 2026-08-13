#### Web Scraping ####
# Web Scraping means automatically collecting data from websites using python

## Examples
### Get headlines from a news site
### Get product prices from Amazon(for learning)
### Get job titles from a careers page

# Important Difference
'''
| Source  | Data Type             |
| ------- | --------------------- |
| API     | Structured (JSON) ✅   |
| Website | Unstructured (HTML) ❌ |

Web Scraping = HTML parsing
'''
# Tools used in Python Web Scraping
## We mainly use two libraries:
### 1. requests
#### Used to download the web page
### 2. BeautifulSoup (bs4)
#### Used to extract data from HTML


# Install required libraries
## pip install requests beautifulsoup4

# Step 1: Fetch a Web Page (requets)
import requests
url = "https://example.com"
response = requests.get(url)
print(response.status_code)
print(response.text)

# # requests.get() --> sends HTTP request
# # response.text ---> raw HTML

# Step 2: Parse HTML (BeautifulSoup) (HTML parsing is the process of analyzing and converting raw HTML code(a string of text) into a structured, usable format)
from bs4 import BeautifulSoup
html = response.text
soup = BeautifulSoup(html, "html.parser")
print(soup)

# Step 3: Extract Specific Data
# Extract Page Title
# print(soup.title.text)

# ## Extract all paragraph text
# for p in soup.find_all("p"):
#     print(p.text)

# How BeautifulSoup Thinks
## HTML looks like this:
# <h1> Welcome</h1>
# <p>This is a paragraph</p>

## BeautifulSoup sees:
### tags --> h1,p
### content --> .text

# Finding elements by tag,class,id
## By tag 
soup.find_all("a") # anchor tags(a)
for a in soup.find_all("a"):
    print(a.text)
## By class
# soup.find_all("div",class_="content")

# ## class_ not class(class is Python keyword)
# # By id
# soup.find(id="main")
# for id in soup.find_all("id"):
#     print(id.text)
# title = soup.find("h1")

# if title:
#     print(title.text)
# else:
#     print("No h1 tag found")

# # Realistic Mini Example
# import requests
# from bs4 import BeautifulSoup
# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"html.parser")
# title=soup.find("h1")
# print(title.text)


### Real-WEBSITE SCRAPING

# https://quotes.toscrape.com

## This is legal, static html(no js issues), clean structure, used worldwide for learning

## In this website we have
'''
<div class="quote">
    <span class="text">“The world as we have created it...”</span>
    <small class="author">Albert Einstein</small>
    <a class="tag">change</a>
</div>

'''
# So we have:
## div with class "quote"
## span with class "text"
## small with class "author"

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

# Scrape ALL quotes(find_all)
quotes = soup.find_all("div",class_="quote")
print("Total quotes found:",len(quotes))

# Extract quote text and author
for q in quotes:
    text = q.find("span",class_="text").text
    author = q.find("small",class_="author").text
    print(text)
    print("-",author)
    print("-" * 40)

# Understanding what is happening
## find_all("div",class_="quote")
### Returns a list of all quotes

# Inside each quote
q.find("span",class_="text") # one element
q.find("small",class_="author")
# These return single tags, so .text works safely

# Scrape all authors only
authors = soup.find_all("small",class_="author")
for a in authors:
    print(a.text)
# Scrape all tags(anchor <a>)
tags = soup.find_all("a",class_="tag")
for tag in tags:
    print(tag.text)

divs = soup.find_all("div",class_="quote")
for div1 in divs:
    print(div1.text)

## Web Scraping involves sending HTTP requets to fetch HTML and using BeautifulSoup to parse and extract specific elements using tags, classes, or ids

import requests
from bs4 import BeautifulSoup

url ="https://gitgrade-repo-mirror.streamlit.app/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print(soup)

divs = soup.find_all("div",class_="root")
for d in divs:
    print(d.text)