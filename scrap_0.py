import requests
from bs4 import BeautifulSoup
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'
]

headers = {
    'User-Agent': random.choice(user_agents)
}
product_links = []
for x in range (1,5):
    r= requests.get(f'https://www.cel.ro/laptop-laptopuri/0a-{x}')
    soup = BeautifulSoup(r.content, 'lxml')

    product_list = soup.find_all('div', class_ = 'product_data productListing-tot')
    for item in product_list:
        top_area_divs = item.find_all('div', class_='topArea')
        for top_area in top_area_divs:
            product_images = top_area.find_all('div', class_='productListing-poza')
            for image_div in product_images:
                links = image_div.find_all('a', href=True)
                for link in links:
                    # print(link['href']) //debug
                    product_links.append(link['href'])

# print (len(product_links)) # debug

for p in product_links:
    r= requests.get(p, headers= headers)  
    soup = BeautifulSoup(r.content, 'lxml')
    price = soup.find('span', id='product-price').text.strip() 
    name = soup.find('h1', id='product-name').text.strip()
    product = {
    'name' : name,
    'price RON' : price,

}
    print(product)  