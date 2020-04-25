# A python script to retrieve random Wikipedia articles.
# Every article is written in a .txt file and saved in a new directory under current working directory.
# Based on Wikipedia-API 0.5.4: https://pypi.org/project/Wikipedia-API/
# and wikipedia 1.4.0: https://pypi.org/project/wikipedia/

import wikipediaapi
import wikipedia
import time
import os

NUMBER_OF_WIKI_ARTICLES = 100

wiki_wiki = wikipediaapi.Wikipedia('en')

current_working_directory = os.getcwd() + "/Wiki Articles"

if not (os.path.isdir(current_working_directory)):
	try:
		os.mkdir(current_working_directory)
	except OSError:
		print("OS Error: Unable to create directory.")

articles_written = 0

start_time = time.time()

for article in range(NUMBER_OF_WIKI_ARTICLES):

	title = wikipedia.random(1)
	page = wiki_wiki.page(title)

	txt_file_name = title + ".txt"
	try:
		with open(os.path.join(current_working_directory, txt_file_name), "w", encoding = "utf-8") as file:

			file.write(page.text)
			articles_written += 1
	except IOError:
		print("I/O Error: Unable to write file %s" % txt_file_name)

finish_time = time.time()
elapsed_time = finish_time - start_time
print("Written %d articles in %.3f seconds." % (articles_written, elapsed_time))
print("Average writting time: %.3f seconds." % (elapsed_time / articles_written))
