# eshop.gr/crazysundays Web Scraper
A python script that retrieves all discounted products and outputs them in both json and csv format.

# Site Discription
[eshop.gr](https://www.e-shop.gr/) is one of Greece's largest web markets of technology, gadgets and more.

Every Sunday eshop.gr posts a list of discounted products on [eshop.gr/crazysundays](https://www.e-shop.gr/crazysundays). 
All offers last for a week, then a new list is posted.

# Dependencies
All python modules used:
1. **requests**
2. **BeautifulSoup**
3. **json**
4. **csv**
5. **date**
6. **lxml**

# Note
UTF8 encoding was used due to greek letters being contained in one or more scraped data. This way every letter is preserved as it originally appears in the site.
