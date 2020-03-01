#!/usr/bin/env python
# coding: utf-8

# ### Import dependencies

# In[146]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint
import re


# ### NASA Mars News

# In[204]:


nasa_news_r = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest").text
#nasa_news_r
soup = BeautifulSoup(nasa_news_r, 'html.parser')
#pprint(soup)


# In[205]:


# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.
news_title = soup.find_all('div', class_="content_title")[0].text
news_p = soup.find_all('div', class_="rollover_description_inner")[0].text

news_title, news_p


# ### Space Images - Featured Image

# In[203]:


# * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# * Use requests to get the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
jpl_mars_r = requests.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars").text

# * Make sure to find the image url to the full size `.jpg` image.

# * Make sure to save a complete url string for this image.
soup = BeautifulSoup(jpl_mars_r, 'html.parser')
feaured_image_url = "www.jpl.nasa.gov" + soup.find_all('a', class_="fancybox")[0]["data-fancybox-href"]
feaured_image_url


# ### Mars Weather

# In[208]:


# * Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) 
# and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report 
# as a variable called `mars_weather`.


# In[538]:


mars_weather_r = requests.get("https://twitter.com/marswxreport?lang=en").text
soup = BeautifulSoup(mars_weather_r, 'html.parser')
soup


# In[540]:


mars_weather = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[0].text.strip("\n")
mars_weather


# ### Mars Facts

# In[244]:


# * Visit the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape 
# the table containing facts about the planet including Diameter, Mass, etc.

# * Use Pandas to convert the data to a HTML table string


# In[282]:


mars_facts_df = pd.read_html("http://space-facts.com/mars/")[0]
mars_facts_df


# ### Mars Hemispheres

# In[433]:


# * Visit the USGS Astrogeology site [here]
# (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
# to obtain high resolution images for each of Mar's hemispheres.

# * You will need to click each of the links to the hemispheres in order to find the image url 
# to the full resolution image.

#  * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title
# containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

# * Append the dictionary with the image url string and the hemisphere title to a list. 
# This list will contain one dictionary for each hemisphere.


# In[519]:


mars_hemispheres_r = requests.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars").text
soup = BeautifulSoup(mars_hemispheres_r, 'html.parser')
#pprint(soup)


# In[523]:


hemispheres = [{'title': e.text.strip(' Enhanced'), 'img_url':("https://astrogeology.usgs.gov" + e['href'])} for e in soup.find_all(class_="itemLink product-item")]
hemispheres


# In[ ]:




