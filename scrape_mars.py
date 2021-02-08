from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = "https://mars.nasa.gov/news/"
browser.visit(url)

html = browser.html
soup = bs(browser.html, 'html.parser')
results = soup.select_one('ul.item_list li.slide')
mars_title = results.find('div', class_="content_title").get_text()
mars_article = results.find('div', class_="article_teaser_body").get_text()
url3 = 'https://space-facts.com/mars/'
mars_table = pd.read_html(url3)
mars_table_df = mars_table[0]
mars_table_html = mars_table_df.to_html()
mars_table_html = mars_table_html.replace('\n', '')
mars_table_df.to_html('mars_table.html')
url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url4)
results = soup.find_all('div', class_="item")
link_url = "https://astrogeology.usgs.gov/"
hemisphere_image_urls = []
for result in results:
    title = result.find('h3').text
    image_link = link_url + result.find('a')['href']
    browser.visit(image_link)
#   links_found = browser.links.find_by_partial_text('Sample')
    
#   images = soup.select_one('div', class_="downloads")
#   image_url = images.find('a')['href']
#   image_url = soup.find('li','a')['href']
#   image_url = images.find.1i.a["href"]
        
#     links_found = browser.find_by_css('.main').links.find_by_partial_text('for Example.com')        
    info = {"title": title, "image_url": image_link}
    hemisphere_image_urls.append(dict(info))
browser.quit()