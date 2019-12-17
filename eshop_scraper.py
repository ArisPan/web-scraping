import requests
from bs4 import BeautifulSoup
from datetime import date
import json
import csv

url = "https://e-shop.gr/crazysundays"

source = requests.get(url).text

soup = BeautifulSoup(source, "lxml")


def identify_category(product_category):

	if product_category == "PER":
		product_category_final = "Υπολογιστές/Ήχος & Εικόνα/Security/Gadgets"
	elif product_category == "TEL":
		product_category_final = "Τηλεπικοινωνίες"
	elif product_category == "HAP":
		product_category_final = "Λευκές Συσκευές/Μικσοσυσκευές"
	elif product_category == "TLS":
		product_category_final = "Εργαλεία"
	elif product_category == "MSC":
		product_category_final = "Μουσικά Όργανα"
	elif product_category == "EPI":
		product_category_final = "Παιχνίδια"
	elif product_category == "ANA":
		product_category_final = "Είδη Γραφείου"
	elif product_category == "BKS":
		product_category_final = "Βιβλία"
	elif product_category == "DVD":
		product_category_final = "Ταινίες DVD/BlueRay"
	elif product_category == "PL2":
		product_category_final = "Αθλητικά Είδη"
	elif product_category == "PL1":
		product_category_final = "Βρεφικά/Παιδικά"
	else:
		product_category_final = "Ηλεκτρονικά Παιχνίδια"

	return product_category_final


products = []

for product_count, crazy_container in enumerate(soup.find_all("tr", class_ = "crazy-row")):

	product_id = crazy_container.find("span", class_ = "per").b.text
	product_category = product_id.split(".")[0]

	product = dict(

		name = crazy_container.find("a", class_ = "main").b.text,

		initial_price = crazy_container.find("p", class_ = "before-price").text,
		final_price = crazy_container.find("p", class_ = "after-price").text,
		discount = crazy_container.find("td", class_ = "crazy-discount normal").b.text,

		availability = crazy_container.find("tr", class_ = "crazy-status-row").b.text,

		category = identify_category(product_category)
	)

	products.append(product)

csv_file_name = "crazy_sunday(" + date.today().strftime("%b-%d-%Y") + ").csv"

try:
	with open(csv_file_name, "w", encoding = "utf-8") as file:

		field_names = ["name", "category", "initial_price", "final_price", "discount", "availability"]

		csv_writer = csv.DictWriter(file, fieldnames = field_names, delimiter = ",")
		csv_writer.writeheader()

		for item in products:
			csv_writer.writerow(item)

		print(str(product_count) + " products written in file " + csv_file_name)
except IOError:
	print("I/O Error")

json_file_name = "crazy_sunday(" + date.today().strftime("%b-%d-%Y") + ").json"

try:
	with open(json_file_name, "w", encoding = "utf-8") as file:

		json.dump(products, file, indent = 4, ensure_ascii = False)

		print(str(product_count) + " products written in file " + json_file_name)
except IOError:
	print("I/O Error")
