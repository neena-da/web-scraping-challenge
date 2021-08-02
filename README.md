# web-scraping-challenge
Web Scraping Homework - Data Analytics Bootcamp

In this assignment, a web application is built that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### Step 1 - Scraping
#### Jupyter Notebook

* NASA Mars News
Srape the website https://redplanetscience.com/ to get the latest Mars headline and news

* JPL Mars Space Images - Featured Image
Scrape the website https://spaceimages-mars.com/ to get the link to the featured image of Mars

* Mars Facts
Scrape the website https://galaxyfacts-mars.com/ to get the table with the Mars and Earth comparison.

* Mars Hemispheres
Scrape the website https://marshemispheres.com/ to get the picture and title for each of the Mars hemispheres.

* Converted the Jupyter notebook into a Python script called scrape_mars.py and store the return value in Mongo as a Python dictionary.

#### Step 2 - MongoDB and Flask Application

* Created an index route to the Mission to Mars page using Flask. Created a route /scrape that will import scrape_mars.py script and call the scrape function from it.

* Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

#### Guide to Repository

Th Mission to Mars folder contains the below

* mission_to_mars.ipynb Jupyter notebook file used to scrap the required data.
* scrape_mars.py python file to scrape the data and store the retreived data in a dictionary
* app.py with the Flask application
* Folder template containing the index.html file
* Style folder containing the style.css file

The snapshot of the output page has been stored in the Output_Figure folder
