#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import json
import re
from subprocess import call


article_list = []
AIA_article_list = []
DN_article_list = []
BD_article_list = []

### AIA News Articles
source = requests.get("https://www2.smartbrief.com/getLast.action?mode=last&b=AIA")
soup = BeautifulSoup(source.content, "html.parser")
article_list.append({'AIA Articles':''})

articles = soup.find('td', class_="main_content").findAll('div', {"class":"name-73"})
print(len(articles))

for article in articles:
    try:
        articleName = article.find('div', {"data-testid":"copy_headline"}).find("a", target="_blank").text
        print(articleName)

        articleSummary = article.find('div', {"class":"name-100"}).text
        print(articleSummary)

        articleLink = article.find('div', {"data-testid":"copy_headline"}).find("a", target="_blank")['href']
        print(articleLink)

        append = {'Article_Name':articleName, 'Article_Summary':articleSummary, 'Article_Link':articleLink}
        AIA_article_list.append(append)
        print(" ")
    except AttributeError:
        continue
print(len(article))
article_list[0]['AIA Articles'] = AIA_article_list


### DefenseNews Article List
source = requests.get("https://www.defensenews.com/")
soup = BeautifulSoup(source.content, "html.parser")
article_list.append({'DefenseNews Articles':''})

block = soup.find('section', {"class":"MainGrid-ui756p-0 BaseLayout__Main-sc-5p6s4f-0 kyjLmS zmBhX t-base__main"}).findAll('div', {"data-gtm-name": re.compile("Home.*")})

for div in block:
    DNArticles = div.findAll('article')
    for article in DNArticles:
        articleName = article.find("a").text
        articleLink = 'https://www.defensenews.com'+article.find("a")['href']
        if len(articleName.split()) < 2:
            articleName
            articleLink
        else:
            print(articleName)
            print('https://www.defensenews.com'+articleLink)
            print(" ")
            append = {'Article_Name':articleName, 'Article_Link':articleLink}
            DN_article_list.append(append)

print(len(block))
print(len(div))
print(len(DNArticles))
print(len(article))

article_list[1]['DefenseNews Articles'] = DN_article_list

# ### BreakingDefense Article List
source = requests.get("https://breakingdefense.com/")
soup = BeautifulSoup(source.content, "html.parser")
article_list.append({'BreakingDefense Articles':''})

wrapper = soup.findAll('div', {"class":"sectional-content"})

for p in wrapper:
    BDArticles = p.findAll('a', {"rel":"bookmark"})
    for article in BDArticles:
        articleName = article.find("span",{"class":"post-loop__title-text"}).text
        articleLink = article['href']
        if len(articleName.split()) < 2:
            articleName
            articleLink
        else:
            print(articleName)
            print('https://www.defensenews.com'+articleLink)
            print(" ")
            append = {'Article_Name':articleName, 'Article_Link':articleLink}
            BD_article_list.append(append)

print(len(block))
print(len(div))
print(len(DNArticles))
print(len(article))

article_list[2]['BreakingDefense Articles'] = BD_article_list



# Article Compilation

article_dict = json.dumps(article_list)
with open("article_dict.json", "w") as outfile:
    outfile.write(article_dict)

Platforms = ['AIA', 'DefenseNews', 'BreakingDefense']
Platforms_List = json.dumps(Platforms) 
with open("Platforms.json", "w") as outfile:
    outfile.write(Platforms_List)


call(["python","email_format.py"])
