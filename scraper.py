import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://www.bridgewaterassociates.com/people'

# opening url and grabbing the web page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')

# grabbing all containers with class name = item-container
containers = page_soup.findAll('div', {'class':'item-container'})

filename = "products.csv"
f = open(filename, 'w')

headers = "first_last_name, position_title, email_trail\n"

f.write(headers)

container = containers[1]

for container in containers:
    brand = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class':'first_last_name'})
    product_name = title_container[0].text
    ship_container = container.findAll('li', {'class':'position_title'})
    # use strip() to remove blank spaces before and after text
    shipping = email_trail[0].text.strip()

    print("name:" + first_last_name)
    print("company title:" + position_title)
    print("possible email permutations:" + email_trail)

    f.write(brand + ',' + product_name.replace(',' , '|') + ',' + shipping + '\n')

f.close()


