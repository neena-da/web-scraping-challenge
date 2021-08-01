# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd
import datetime as dt

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_main_title, news_paragraph = mars_news(browser)

    data = {
        "news_title": news_main_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(browser),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    browser.quit()
    return data

# Function to get the news title and news paragraph
def mars_news(browser):
    url_mars_news = "https://redplanetscience.com/"
    browser.visit(url_mars_news)
    time.sleep(1)

    html_news = browser.html
    soup_news = bs(html_news, "html.parser")

    try:
        # Get the News Title
        news_title = soup_news.find_all('div', class_='content_title')[0].text

        # Get the News Paragraph
        news_para = soup_news.find_all('div', class_='article_teaser_body')[0].text
    except AttributeError:
        return None, None
    
    return news_title, news_para

# Function to get the current Featured Mars Image
def featured_image(browser):
    url_space_image = "https://spaceimages-mars.com/"
    browser.visit(url_space_image)
    time.sleep(1)

    browser.links.find_by_partial_text('FULL IMAGE').click()

    html_image = browser.html
    soup_image = bs(html_image, "html.parser")

    try:
        # Get the url for the current Featured Mars Image
        # featured_image_link = soup_image.find_all('img', class_='fancybox-image')[0]['src']

        # # Get the Full link
        # featured_image_url = url_space_image + featured_image_link
        featured_image_url = soup_image.find_all('div', class_='fancybox-outer')[0].img['src']
        featured_image_link = url_space_image + featured_image_url
    except AttributeError:
        return None, None

    return featured_image_link

# Function to visit galaxyfacts-mars.com to get the table containing facts about mars
def mars_facts(browser):
    url_facts = "https://galaxyfacts-mars.com/"
    browser.visit(url_facts)
    time.sleep(1)

    # Scrape page into Soup
    html_facts = browser.html
    soup_facts = bs(html_facts, "html.parser")

    try:
        # Get the table with the Mars facts
        tables = pd.read_html(url_facts)
        mars_table = tables[0]
        mars_table = mars_table.rename(columns={0: 'Description', 1: 'Mars', 2: 'Earth'})
        mars_table = mars_table.set_index('Description')
        mars_html = mars_table.to_html(justify='left', classes=["table-bordered", "table-striped", "table-sm", "isi"])
    except AttributeError:
        return None, None

    return mars_html

# Function to visit marshemispheres.com to get the pictures for the mars hemispheres
def hemispheres(browser):
    hem_list = ['cerberus', 'schiaparelli', 'syrtis', 'valles']
    hem_dict = {}
    hemisphere_image_urls = []

    url_hem_base = 'https://marshemispheres.com/'

    for hem in hem_list:
        url_hem = f"{url_hem_base}{hem}.html"
    
        browser.visit(url_hem)
        time.sleep(1)
    
        html_hem = browser.html
        soup_hem = bs(html_hem, "html.parser")
        try:
            hem_head_class = soup_hem.find_all('div', class_='cover')
            hem_heading = hem_head_class[0].h2.text
    
            hem_image = soup_hem.find_all('div', class_='downloads')
            hem_full_image = hem_image[0].li.a['href']
            hem_link = url_hem_base + hem_full_image
    
            hem_dict = {"title": hem_heading, "img_url": hem_link}
            hemisphere_image_urls.append(hem_dict)
        except AttributeError:
            return None, None

    return hemisphere_image_urls