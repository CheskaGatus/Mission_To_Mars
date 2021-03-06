# Mission to Mars

The purpose of this project is to build a web application that scrapes various websites for data related to the mission to Mars. It displays information in a single HTML page. 

## Scraping

Scraping is done using Jupyter Notebook, BeautifulSoup, Pandas, and Splinter.


### NASA Mars News

Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest news title and paragraph text.


### JPL Mars Space Images - Featured Image

Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
Use splinter to navigate the site and find the full size jpg image url for the current Featured Mars Image.

### Mars Weather

Scrape the latest Mars weather tweet from Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en).

### Mars Facts

Visit the Space Facts webpage, Mars facts page [here](https://space-facts.com/mars/).
Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Use Pandas to convert the data to HTML table string.

### Mars Hemispheres

Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mars' hemispheres.

Click each of the links to the hemispheres in order to find the image url to the full resolution image.

Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


- - -

## MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Convert Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all scraping code from above and return one Python dictionary containing all of the scraped data.

* Create a route called `/scrape` that will import `scrape_mars.py` script and call `scrape` function.

* Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
- - -