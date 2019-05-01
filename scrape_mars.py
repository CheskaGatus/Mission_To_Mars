def scrape():

	# Dependencies
	from bs4 import BeautifulSoup as bs
	import pandas as pd
	from splinter import Browser

	executable_path = {'executable_path': 'resources/chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)

	# Create Mission to Mars global dictionary that can be imported into MongoDB
	mars_info = {}

	### NASA Mars News
	# Scrape the NASA Mars News Site and collect the latest news title and paragraph text.
	
	url_news = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	
	browser.visit(url_news)

	soup_news = bs(browser.html, 'html.parser')

	#print(soup_news.prettify())

	# Find latest news title
	news_title = soup_news.find('div', class_='content_title').text

	# Dictionary entry for news title
	mars_info['news_title'] = news_title

	# Find latest news paragraph
	news_paragraph = soup_news.find('div', class_='article_teaser_body').text
	
	# Dictionary entry for news paragraph
	mars_info['news_paragraph'] = news_paragraph


	### JPL Mars Space Images - Featured Image
	# Use splinter to navigate the site and find the image url for the current Featured Mars Image

	url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	
	browser.visit(url_image)

	soup_image = bs(browser.html, 'html.parser')

	#print(soup_image.prettify())

	image = soup_image.find_all('a', class_ ="fancybox")[1]['data-fancybox-href']
	#print(image)

	# Concatenate website url with scrapped route
	featured_image_url = 'https://www.jpl.nasa.gov' + image

	# Dictionary entry for Mars featured image
	mars_info['featured_image_url'] = featured_image_url
	
	
	### Mars Weather from Twitter
	# Scrape the latest Mars weather tweet from Mars Weather twitter account.

	url_twitter = 'https://twitter.com/marswxreport?lang=en'
	
	browser.visit(url_twitter)

	soup_weather = bs(browser.html, 'html.parser')

	#print(soup_weather.prettify())

	# Display mars weather details
	mars_weather = soup_weather.find_all('p', class_ = 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text.split("pic")[0]
	
	# Dictionary entry for Mars weather from twitter
	mars_info['mars_weather'] = mars_weather



	###### I need to remove pic.twitter.com/v0syJv5akT to the above result




	### Mars Facts from Space Facts
	# Visit the Space Facts webpage, mars facts page. 
	# Use Pandas to scrape the table containing facts about Mars including Diameter, Mass, etc.
	# Use Pandas to convert the data to a HTML table string

	url_facts = 'https://space-facts.com/mars/'
	
	browser.visit(url_facts)


	# Use Panda's `read_html` to parse the url
	facts_df = pd.read_html(url_facts)[0]

	# Rename columns
	facts_df.columns = ['Description', 'Value']

	# Set description column as index
	facts_df.set_index('Description', inplace=True)

	# Dictionary entry for Mars Facts from Space Facts
	mars_info['mars_facts'] = facts_df.to_html()

	### Mars Hemispheres
	# Visit the USGS Astrogeology site to obtain high resolution images for each of Mars' hemispheres.

	url_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	
	browser.visit(url_hemispheres)

	soup_hemisphere = bs(browser.html, 'html.parser')

	#print(soup_hemisphere.prettify())

	results = soup_hemisphere.find_all('div', class_ = 'description')

	hemisphere_image_urls = []

	for result in results:
		
		# Get hemisphere name and save in variable called title
		title = result.find('h3').text
		
		# Get links to the hemispheres and save in variable called url
		partial_url = result.find('a', class_="itemLink product-item")['href']
		url = 'https://astrogeology.usgs.gov/' + partial_url
		
		# Click each of the url to find the full resolution hemisphere image. Save in variable called img_url).
		browser.visit(url)
		soup_imgs = bs(browser.html, 'html.parser')
		img_url = soup_imgs.find('div', class_='downloads').li.a['href']
		
		# Use a Python dictionary to store the data using the keys img_url and title. 
		# Append the dictionary with the hemisphere title and image url string to a list. 
		# This list will contain one dictionary for each hemisphere.
		hemisphere_image_urls.append({'title':title, 'img_url':img_url})


	mars_info['hemisphere_image_urls'] = hemisphere_image_urls

    browser.quit()

    return mars_info