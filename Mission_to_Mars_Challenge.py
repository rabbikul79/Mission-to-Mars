# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# Scrape the Title
slide_elem.find('div', class_='content_title')
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url
# Create dataframe 
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df
# Convert to html
df.to_html()
# Quit browser
browser.quit()
# 1. Use browser to visit the URL 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Get a list of the hemispheres
links = browser.find_by_css('a.product-item img')

# Loop through links, click each, find the anchor and return the href
for i in range(len(links)):
    hemisphere = {}
    
    # Click each link
    browser.find_by_css('a.product-item img')[i].click()
    
    # Find the anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    # Get the title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # Append to list
    hemisphere_image_urls.append(hemisphere)
    
    # Go back
    browser.back()
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls
# 5. Quit the browser
browser.quit()
