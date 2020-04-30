# Random Wikipedia Article Scraper
A python script to retrieve random Wikipedia articles.\
Not a scraper per se since Python wrappers of Wiki API were used to retrieve the articles.\
Every article is written in a .txt file and saved in a new directory under current working directory.\
Every file is named after each articles title.

# Python wrappers of Wiki API
1. [Wikipedia-API 0.5.4](https://pypi.org/project/Wikipedia-API/)
2. [wikipedia 1.4.0](https://pypi.org/project/wikipedia/)

# Versioning
**Version 1** comprises basic functionality described above.\
**Version 2** includes added features like a progress bar, courtesy of [tqdm](https://github.com/tqdm/tqdm).\
A Wiki article may include characters in its title which are invalid as a file name. In Windows this characters are <>:"/\\|?*
This issue is addressed in version 2 by adding a second pass to the rejected file names after having stripped all invalid characters.

# Dependencies
All python modules used:
1. **tqdm**
2. **wikipediaapi**
3. **wikipedia**

**Install using pip:**
```
pip install tqdm
pip install Wikipedia-API
pip install wikipedia
```
To execute just type `python wiki_scraper2.py`
