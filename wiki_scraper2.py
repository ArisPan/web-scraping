# A python script to retrieve random Wikipedia articles.
# Every article is written in a .txt file and saved in a new directory under current working directory.
# Based on Wikipedia-API 0.5.4: https://pypi.org/project/Wikipedia-API/
# and wikipedia 1.4.0: https://pypi.org/project/wikipedia/

# Smart progress bar with the help of tqdm: https://github.com/tqdm/tqdm

from tqdm import tqdm
import wikipediaapi
import wikipedia
import time
import os

NUMBER_OF_WIKI_ARTICLES = 1000

wiki_wiki = wikipediaapi.Wikipedia('en')

current_working_directory = os.getcwd() + "/Wiki Articles"

if not (os.path.isdir(current_working_directory)):
	try:
		os.mkdir(current_working_directory)
	except OSError:
		print("OS Error: Unable to create directory.")

articles_written = 0
article_titles_not_written = []
article_pages_not_written = []

print("Retrieving articles and writting them to file.")

start_time = time.time()

for article in tqdm(range(NUMBER_OF_WIKI_ARTICLES)):

	title = wikipedia.random(1)
	page = wiki_wiki.page(title)

	txt_file_name = title + ".txt"
	try:
		with open(os.path.join(current_working_directory, txt_file_name), "w", encoding = "utf-8") as file:

			file.write(page.text)
			articles_written += 1
	except IOError:
		article_titles_not_written.append(txt_file_name)
		article_pages_not_written.append(page)

if len(article_titles_not_written) > 0:

	print("%d files could not be written, trying again." % len(article_titles_not_written))
	for count in tqdm(range(len(article_titles_not_written))):

		# File titles can't contain <>:"/\|?* characters.
		# So strip 'em.
		txt_file_name = article_titles_not_written[count].translate({ord(i): None for i in '<>:"/\\|?*'})

		try:
			with open(os.path.join(current_working_directory, txt_file_name), "w", encoding = "utf-8") as file:

				file.write(article_pages_not_written[count].text)
				articles_written += 1
		except IOError:
			print("I give up. File %s could not be written." % txt_file_name)

finish_time = time.time()
elapsed_time = finish_time - start_time
print("Written %d articles in %.3f seconds." % (articles_written, elapsed_time))
print("Average writting time: %.3f seconds." % (elapsed_time / articles_written))
