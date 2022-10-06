import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
						Chrome/104.0.5112.124 YaBrowser/22.9.2.1500 Yowser/2.5 Safari/537.36"}

def get_item_url():
	for el in range(1, 8):

		url = f'https://scrapingclub.com/exercise/list_basic/?page={el}'
		response = requests.get(url, headers= headers)
		soup = BeautifulSoup(response.text, 'lxml') # html.parser
		data = soup.find_all('div', class_= 'col-lg-4 col-md-6 mb-4')

		for item in data:
			url_item = 'https://scrapingclub.com' + item.find('a').get('href')
			yield url_item


def get_array_item():
	for url_item in get_item_url():
		response = requests.get(url_item, headers= headers)

		sleep(3)

		soup = BeautifulSoup(response.text, 'lxml') # html.parser

		item = soup.find('div', class_= 'card mt-4 my-4')

		name_item = item.find('h3', class_= 'card-title').text.replace('\n', '')
		price_item = item.find('h4').text.replace('\n', '')
		description_item = item.find('p', class_= 'card-text').text.replace('\n', '')
		url_img_item = 'https://scrapingclub.com' + item.find('img', class_= 'card-img-top img-fluid').get('src')

		yield name_item, description_item, price_item, url_img_item
