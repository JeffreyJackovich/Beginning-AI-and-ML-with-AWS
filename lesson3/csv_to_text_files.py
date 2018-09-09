import csv
import os

row_list = []


# manually export CSV from MySQL - 
data_dir = os.getcwd() + "\\mysql_output\\"
with open(data_dir + 'all_infozine_articles_export_3.csv', 'r', encoding="utf-8") as in_file:
	for row in in_file:
		
		readCSV = csv.reader(in_file)
		for row in readCSV:
			article_description = row[2]
			# articleContent = row[5]
			articleId = row[6]
			row_list.append(row)



text_file_directory_output = os.getcwd() + "\\text_files\\infozine__all_categories_output\\"
for line in row_list:
	article_description = line[2]
	# article_content = line[5]
	articleId = line[6]
	category = line[4]
	out_file = open(text_file_directory_output + "category_{0}__articleID_{1}.txt".format(category, articleId), 'w+', encoding="utf-8")
	out_file.write(article_description)
	#out_file.write(articleContent)
out_file.close() 