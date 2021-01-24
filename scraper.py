from selenium import webdriver
import re
from xlwt import Workbook
from openpyxl import Workbook

# Enter Local Path to Driver Chrome For Browser Support
PATH = "/Users/daniel/code/scraper/chromedriver"

# Instantiate Chrome Window
driver = webdriver.Chrome(PATH)

# Create New Workbook and open the current active window
workbook = Workbook()
sheet = workbook.active



# Open Text File of Website List
with open('websites.txt') as websiteSpreadsheet:
	
	for line in websiteSpreadsheet: # Iterate through all lines
		
		# Grab Website URL and Set As Source
		driver.get(line)
		LoadedPageSource = driver.page_source

		# ReGEX find all email matches within HTML of website
		FoundEmails = re.findall(r'[\w\.-]+@[\w\.-]+', LoadedPageSource)
		for email in FoundEmails:
			print(sheet.cell_value(email, 0))
			sheet["B1"] = email
			websiteSpreadsheet.write(email) + (',' (',' , '|') + ',' + '\n')
			print(email) # Print the Email to Terminal to Show List
	
# Save and Close Excel Workbook When Finished Executing 
workbook.Save()
workbook.Close()

# Quit Open Sheet To Signal Execution Done
sheet.Quit()