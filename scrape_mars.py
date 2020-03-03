# Import dependencies
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint

def scrape():

	mars_scrapped = {}

	# NASA Mars News
	nasa_news_r = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest").text
	soup = BeautifulSoup(nasa_news_r, 'html.parser')

	news_title = soup.find_all('div', class_="content_title")[0].text.replace("\n","")
	news_p = soup.find_all('div', class_="rollover_description_inner")[0].text.replace("\n","")

	mars_scrapped["mars_news_title"] = news_title
	mars_scrapped["mars_news_p"] = news_p


	# Space Images - Featured Image
	jpl_mars_r = requests.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars").text
	soup = BeautifulSoup(jpl_mars_r, 'html.parser')

	feaured_image_url = "https://www.jpl.nasa.gov" + soup.find_all('a', class_="fancybox")[0]["data-fancybox-href"]

	mars_scrapped["featured_img"] = feaured_image_url


	# Mars Weather
	mars_weather_r = requests.get("https://twitter.com/marswxreport?lang=en").text
	soup = BeautifulSoup(mars_weather_r, 'html.parser')

	mars_weather = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[0].text.replace("\n"," ")[:-26]

	mars_scrapped["mars_weather"] = mars_weather


	# Mars Facts
	mars_facts_df = pd.read_html("http://space-facts.com/mars/")[0].rename(columns={0:"Description", 1:"Values"})
	mars_facts = mars_facts_df.to_html(index=False, header=True, classes="table")

	mars_scrapped["mars_facts"] = mars_facts


	# Mars Hemispheres
	mars_hemispheres_r = requests.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars").text
	soup = BeautifulSoup(mars_hemispheres_r, 'html.parser')

	hemispheres = [{'title': e.text.strip(' Enhanced'), 'img_url':("https://" + "astropedia." + "astrogeology.usgs.gov" + e['href'] + '.tif/full.jpg').replace("search/map", "download")} for e in soup.find_all(class_="itemLink product-item")]
	
	mars_scrapped["mars_hemispheres"] = hemispheres

	### Printing dict ###
	return mars_scrapped