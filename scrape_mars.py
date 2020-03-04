# Import dependencies
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint
import re
import json


def scrape():

    # Main Dict for json string
    mars_scrapped = {}

    ### Nasa News Scraper ###
    nasa_news_r = requests.get(
        "https://mars.nasa.gov/api/v1/news_items/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    )
    data = nasa_news_r.json()
    news_title = data["items"][0]["title"]
    news_p = data["items"][0]["description"]

    mars_scrapped["mars_news_title"] = news_title
    mars_scrapped["mars_news_p"] = news_p

    ### Featured Image Scraper ###
    jpl_mars_r = requests.get(
        "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    ).text
    soup = BeautifulSoup(jpl_mars_r, "html.parser")

    feaured_image_url = (
        "https://www.jpl.nasa.gov"
        + soup.find_all("a", class_="fancybox")[0]["data-fancybox-href"]
    )

    mars_scrapped["featured_img"] = feaured_image_url

    ### Mars Weather Scraper ###
    mars_weather_r = requests.get("https://twitter.com/marswxreport?lang=en").text
    soup = BeautifulSoup(mars_weather_r, "html.parser")

    mars_weather = soup.find_all(
        "p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"
    )[0].text.replace("\n", " ")[:-26]
    mars_weather = re.sub(r"[^ ]+\.[^ ]+", "", mars_weather)
    mars_scrapped["mars_weather"] = mars_weather

    ### Mars Facts Scraper ###
    mars_facts_df = pd.read_html("http://space-facts.com/mars/")[0].rename(
        columns={0: "Description", 1: "Values"}
    )
    mars_facts = mars_facts_df.to_html(index=False, header=True, classes="table")

    mars_scrapped["mars_facts"] = mars_facts

    ### Mars Hemispheres Scraper ###
    mars_hemispheres_r = requests.get(
        "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    ).text
    soup = BeautifulSoup(mars_hemispheres_r, "html.parser")

    hemispheres = [
        {
            "title": e.text.strip(" Enhanced"),
            "img_url": (
                "https://"
                + "astropedia."
                + "astrogeology.usgs.gov"
                + e["href"]
                + ".tif/full.jpg"
            ).replace("search/map", "download"),
        }
        for e in soup.find_all(class_="itemLink product-item")
    ]

    mars_scrapped["mars_hemispheres"] = hemispheres

    # Printing dict #
    return mars_scrapped
