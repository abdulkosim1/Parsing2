# import requests
# import csv
# from bs4 import BeautifulSoup as BS
# def get_html(url):
#     response = requests.get(url)
#     return response.text
# def get_soup(html):
#     soup = BS(html, 'html.parser')
#     return soup
# def get_data(soup):
#     laptops = soup.find_all('div', class_ = 'ty-column4')
#     # print(laptops)
#     for i in laptops:
#         try:
#             title = i.find('a', class_ ='product-title').text.strip()
#         except AttributeError:
#             title = ''
#         try:    
#             price = i.find('span', class_ ='ty-price-num').text
#         except AttributeError:
#             price = ''
#         try: 
#             image = i.find('img', class_='ty-pict').get('data-ssrc')
#         except AttributeError:
#             image = ''
#         write_csv({
#             'title':title,
#             'price':price,
#             'image':image
#         })

# def write_csv(data):
#     with open('laptops.csv','a') as file:
#         names = ['title', 'price', 'image']
#         write = csv.DictWriter(file,delimiter=',', fieldnames=names)
#         write.writerow(data)


# def main():
#     for i in range(1,79):
#         BASE_URL = f'https://svetofor.info/noutbuki-planshety-bukridery/page-{i}'
#         html = get_html(BASE_URL)
#         soup = get_soup(html)
#         get_data(soup)
#         print(f'Спарсили страницу {i}')

# if __name__ == '__main__':   
#     main()


import requests
import csv
from bs4 import BeautifulSoup as BS
def get_html(url):
    response = requests.get(url)
    return response.text
def get_soup(html):
    soup = BS(html, 'html.parser')
    return soup
def get_data(soup):
    # news = soup.find_all('div',class_='itemList')
    news1 = soup.find_all('div', class_ = 'itemBody')
    for i in news1:
      title = i.find('a').text.strip()
      # print(title)
    # print(news1)
      write_csv({
        'title':title
                  })


def write_csv(data):
    with open('news.csv','a') as file:
        names = ['title']
        write = csv.DictWriter(file,delimiter=',', fieldnames=names)
        write.writerow(data)

for i in range(0,150,30):
  BASE_URL = f'https://vesti.kg/itemlist.html?start={i}'
  html = get_html(BASE_URL)
  soup = get_soup(html)
  get_data(soup)
