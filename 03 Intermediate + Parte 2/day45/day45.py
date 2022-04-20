""" Day 45 """

# ######### BEAUTIFUL SOUP ###########
"""
from bs4 import BeautifulSoup  # Beautiful Soup
# import lxml

with open("website.html", encoding='utf8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)  # <title>Angela's Personal Site</title>
# print(soup.title.name)  # title
# print(soup.prettify())  # Imprime TO DO O CÓDIGO!!!
# print(soup.a)  # primeiro resultado de "a" --> <a href="https://www.appbrewery.co/">The App Brewery</a>
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)  # Todos os resultados de "a"
# [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">
# My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

for tag in all_anchor_tags:
    # print(tag.getText())
    # The App Brewery
    # My Hobbies
    # Contact Me
    # print(tag.get("href"))
    # https://www.appbrewery.co/
    # https://angelabauer.github.io/cv/hobbies.html
    # https://angelabauer.github.io/cv/contact-me.html
    pass

heading = soup.find(name="h1", id="name")
print(heading)  # <h1 id="name">Angela Yu</h1>

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)  # <h3 class="heading">Books and Teaching</h3>
print(section_heading.getText())  # Books and Teaching

company_url = soup.select_one(selector="p a")
print(company_url)  # <a href="https://www.appbrewery.co/">The App Brewery</a>   <------ TRECHO DO "p" ABAIXO!
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>

name = soup.select_one(selector="#name")  # Qdo procurar id necessita usar "#"
print(name)  # <h1 id="name">Angela Yu</h1>

headings = soup.select(".heading")
print(headings)  # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
"""
# ######### QUIZ ###########
"""
Question 1:
This is an unordered list (<ul>) extracted from the BeautifulSoup Home Page. What's the code to get all the anchor
tags (<a>) if we have already made soup from the HTML?

<ul class="simple">
    <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/">这篇文档当然还有
    中文版.</a></p></li>
    <li><p>このページは日本語で利用できます(<a class="reference external" href="http://kondou.com/BS4/">外部リンク</a>)</p></li>
    <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/">이 문서는 한국어
     번역도 가능합니다.</a></p></li>
    <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr">Este
     documento também está disponível em Português do Brasil.</a></p></li>
    <li><p><a class="reference external" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/">Эта 
    документация доступна на русском языке.</a></p></li>
</ul>

Answer: soup.find_all("a") <--- Because there are no other anchor tags in this entire soup, you don't have to specify 
                                the class.

Question 2:
Below is a simplified version of the Beautiful Soup Hall of Fame. The HTML code comes from the Beautiful Soup home page.

If soup was made from the HTML below, how would you extract only the anchor tags from inside the unordered list? (So
excluding the first anchor tag <a name="HallOfFame"><h2>Hall of Fame</h2></a>?

<a name="HallOfFame"><h2>Hall of Fame</h2></a>
<p>Over the years, Beautiful Soup has been used in hundreds of different projects.</p>
<ul>
<li>Alexander Harrowell uses Beautiful Soup to <a href="http://www.harrowell.org.uk/viktormap.html">track the business
 activities</a> of an arms merchant.</li>
<li>The developers of Python itself used Beautiful Soup to <ahref="http://svn.python.org/view/tracker/importer/">migrate
 the Pythonbug tracker from Sourceforge to Roundup</a>.</li>
</ul>

Answer: soup.select("li a") <--- This uses a CSS selector to find all the <a> tags in a <li> tag. Which is what we want.

Question 3:
If we make soup with the HTML code below, how would you get hold of the value of maxlength?
<form method="get" action="/search/">
 <input type="text" name="q" maxlength="255" value=""></input>
</form> 
There's no shame in looking at the documentation!
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Answer: form_tag = soup.find("input")
        max_length = form_tag.get("maxlength")
"""
# ######### Scraping a Live Website ###########
# """
import requests
from bs4 import BeautifulSoup  # Beautiful Soup

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)  # <title>Hacker News</title>
a = soup.title
# print(a.getText())  # Hacker News
# print(soup.title.getText())  # Hacker News

article_tag = soup.find(name="a", class_="titlelink")
# print(article_tag)
# <a class="titlelink" href="https://news.microsoft.com/2022/01/18/microsoft-to-acquire-activision-blizzard-to-bring-
# the-joy-and-community-of-gaming-to-everyone-across-every-device/">Microsoft to Acquire Activision Blizzard</a>
# print(article_tag.getText())  # Microsoft to Acquire Activision Blizzard
# text = article_tag.getText()
# print(text)
# link = article_tag.get("href")
# print(link)
article_upvote = soup.find(name="span", class_="score").getText()

# print(article_text)  # Microsoft to Acquire Activision Blizzard
# print(article_link)  # https://news.microsoft.com/2022/01/18/microsoft-to-acquire-activision-blizzard-to-bring-the-
# joy-and-community-of-gaming-to-everyone-across-every-device/
# print(article_upvote)  # 938 points


articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# print(article_texts)  # ['Microsoft to Acquire Activision Blizzard', 'The Intel Split', 'Show HN:... he sun']
# print(article_links)  # ['https://news.microsoft.com/2022/01/18/microsoft-to-acquire-activisio...solar-probe/621275/']
# print(article_upvotes)  # ['986 points', '40 points', '122 points', '25 points', '169 points',... '63 points']
# print(article_upvotes[0])  # 1011 points
# print(article_upvotes[0].split())  # ['1011', 'points']
# print(article_upvotes[0].split()[0])  # 1011 (string)
# print(int(article_upvotes[0].split()[0]))  # 1023 (integer)
article_upvotes_numbers = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes_numbers)  # [628, 114, 174, 59, 135, 1465, 43, 155, 21, 179, 210, 59, 67, 260, 41, 85,..., 71, 6]

largest_number = max(article_upvotes_numbers)
largest_index = article_upvotes_numbers.index(largest_number)
print(largest_index)  # 5
print(article_texts[largest_index])  # Microsoft to Acquire Activision Blizzard
print(article_links[largest_index])  # https://news.microsoft.com/2022/01/18/microsoft-to-acquire-activision-bl...ice/

# """
# ######### 100 Movies that You Must Watch ###########
# """
import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())  # site to_do.... muita informação

listicle_items = soup.find_all(class_="listicle-item")
# print(listicle_items)

titles = []
i = 100

for listicle_item in listicle_items:
    titles.append(f'{i}) {listicle_item.select_one("img").get("alt")}')
    i -= 1

titles = titles[::-1]  # Inverte a ordem [start:stop:ordem]
print(titles)

with open("movies.txt", "w") as file:
    for title in titles:
        file.write(f"{title}\n")
# """

