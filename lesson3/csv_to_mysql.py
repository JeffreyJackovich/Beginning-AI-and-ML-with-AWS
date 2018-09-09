import csv
import os
import pymysql

row_list = []

#mysql
conn = pymysql.connect(db='<your db name>',
						host='<your host name>',
						port='<port number>',
						user='administrator',
						password='<your password>',
						use_unicode=True,
						charset='utf8')

# manual CSV export from MySQL
with open('topic-terms.csv', 'r', encoding="utf-8") as in_file:
	for row in in_file:
		
		readCSV = csv.reader(in_file)

		for row in readCSV:
			article_description = line[2]
			# articleContent = row[5]
			articleId = row[6]
			row_list.append(row)

#import all articles to MySQL database
with conn.cursor() as cur:
	for row in articles:
		cur.execute("CREATE TABLE IF NOT EXISTS tech_xplore_topic_terms (id INTEGER NOT NULL AUTO_INCREMENT, topic INTEGER, \
														term VARCHAR(800) NOT NULL, \
														weight FLOAT NOT NULL,\
									                    PRIMARY KEY (id) );") 
		cur.execute("INSERT IGNORE INTO linkedTopicDB2.tech_xplore_topic_terms (topic, term, weight) VALUES (%s, %s, %s)", (row[0], row[1], row[2])
	conn.commit()
	conn.close()