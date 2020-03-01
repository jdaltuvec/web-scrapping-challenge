# Import dependencies
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint
import re


# NASA Mars News
nasa_news_r = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest").text
soup = BeautifulSoup(nasa_news_r, 'html.parser')

news_title = soup.find_all('div', class_="content_title")[0].text
news_p = soup.find_all('div', class_="rollover_description_inner")[0].text


# Space Images - Featured Image
jpl_mars_r = requests.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars").text
soup = BeautifulSoup(jpl_mars_r, 'html.parser')

feaured_image_url = "www.jpl.nasa.gov" + soup.find_all('a', class_="fancybox")[0]["data-fancybox-href"]


# Mars Weather
mars_weather_r = requests.get("https://twitter.com/marswxreport?lang=en").text
soup = BeautifulSoup(mars_weather_r, 'html.parser')

mars_weather = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[0].text.strip("\n")


# Mars Facts
mars_facts_df = pd.read_html("http://space-facts.com/mars/")[0]



# Mars Hemispheres
mars_hemispheres_r = requests.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars").text
soup = BeautifulSoup(mars_hemispheres_r, 'html.parser')

hemispheres = [{'title': e.text.strip(' Enhanced'), 'img_url':("https://astrogeology.usgs.gov" + e['href'])} for e in soup.find_all(class_="itemLink product-item")]
