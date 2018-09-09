import feedparser
import pymysql
from bs4 import BeautifulSoup 
import requests
import re 
#import string

#mysql connection 
conn = pymysql.connect(db='<your db name>',
						host='<your host name>',
						port='<port number>',
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')


# use_unicode=True,
# charset='utf8'
# UnicodeEncodeError: 'latin-1' codec can't encode character '\u2019' in position 237: ordinal not in range(256)


 
# 1. Get all usable category links
# 2. Start at root categroy page and get article links.  ex: http://www.infozine.com/news/topics/op/topicsView/tid/5/  
# 3. Loop through "next 15 articles" category pages for additional article links.   ex: http://www.infozine.com/news/topics/op/topicsView/tid/5/next/15 
# 4. Loop through article links and parse article_content 


url = 'http://www.infozine.com/news/stories/op/storiesView/sid/1338/'
text = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(text.content)


category_urls_list = []
article_urls_list = []

# 1. Get all usable category links
topics = soup.find('div', {'class': 'menuTopic'})
rows = topics.findAll('li')
for li in rows:
    link = li.find('a').get('href')
    category_urls_list.append(link)


# 2. Start at root categroy page and get article links.  ex: http://www.infozine.com/news/topics/op/topicsView/tid/5/  

for category_url in category_urls_list:
	category_page_response = requests.get(category_url, headers={'User-Agent':'Mozilla/5.0'})
	category_page_soup = BeautifulSoup(category_page_response.content)
	article_rows = category_page_soup.findAll('div', attrs={"class" : "topicHeadline"})
	for 





		# parse article_content
		# headers={'User-Agent':'Mozilla/5.0'}
		resp = requests.get(link, headers={'User-Agent':'Mozilla/5.0'})
		soup = BeautifulSoup(resp.content)
		contentArticle = soup.find('div', attrs={"class" : "contentArticle"})
		total_article_content = contentArticle.text
		 


		# extend() - Iterates over its arguments adding each RSS element to the list (i.e. row_list).
		row_list.extend((title, description, link, article_content, category, pubDate))
		# append() - Appends objects at the end off the list (i.e. articles_list).
		articles_list.append(row_list)



# import all articles to MySQL database
# avoid importing duplicate articles 
with conn.cursor() as cur:
	for row in articles_list:
		cur.execute("CREATE TABLE IF NOT EXISTS all_infozine_articles (id INTEGER NOT NULL AUTO_INCREMENT, title VARCHAR(350), \
														description VARCHAR(2000), \
														link VARCHAR(350) NOT NULL,\
									                    article_content VARCHAR(8000), \
									                    category VARCHAR(350),\
									                    pubDate VARCHAR(150),\
									                    PRIMARY KEY (link), \
									                    KEY id (id) );") 
		cur.execute("INSERT IGNORE INTO linkedTopicDB2.all_infozine_articles (title, description, link, article_content, category, pubDate) VALUES (%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))
	conn.commit()
	conn.close()