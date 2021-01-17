from selenium import webdriver
import re
from xlwt import Workbook
from openpyxl.reader.excel import load_workbook

# Enter Local Path to Driver Chrome For Browser Support
PATH = "/Users/daniel/code/scraper/chromedriver"

# Instantiate Chrome Window
driver = webdriver.Chrome(PATH)

# Open Text File of Website List
with open('websites.txt') as f:
	
	for line in f: # Iterate through all lines
		
		# Grab Website URL and Set As Source
		driver.get(line)
		LoadedPageSource = driver.page_source

		# ReGEX find all email matches within HTML of website
		FoundEmails = re.findall(r'[\w\.-]+@[\w\.-]+', LoadedPageSource)
		for email in FoundEmails:
			print(email) # Print the Email to Terminal to Show List
