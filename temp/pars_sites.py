import requests
import fake_useragent
from bc4 import BeautifulSoup

url = 'https://allo.ua/ua/roboty-pylesosy/'
user = fake_useragent.UserAgent().random
#print(user)
headers = {"user-agent": user}

response = requests.get(url, headers=headers)
#print(response.text)
soup = BeautifulSoup(response.text,"lxml")
#print(soup)

all_product = soup.find('div', class_='products-layout__container products-layout--grid')

product_list = all_product.find_all('div', class_='product-card')
print(product_list[0])

for i in range(len(product_list)):
    product_title = product_list[i].find('a', class_='product-card__title')
    print(product_title.text)


# response = requests.get(url)
# print(response.text)
