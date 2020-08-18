# Google-Image-Scraping

Web scraping can be defined as:

“the construction of an agent to download, parse, and organize data from the web in an automated manner.”

Or in other words: instead of a human end-user clicking away in their web browser and copy-pasting interesting parts into, say, a spreadsheet, web scraping offloads this task to a computer program which can execute it much faster, and more correctly, than a human can.

Why is Python a suitable language to use for Web Scraping?

It has the most elaborate and supportive ecosystem when it comes to web scraping. While many languages have libraries to help with web scraping, Python’s libraries have the most advanced tools and features.

Some python libraries for web scraping:
-Beautiful Soup
-Scrapy
-Requests
-LXML
-Selenium

Here, we’ll focus on Beautiful Soup and Selenium and how to scrap images from google image.

Why Selenium? Isn’t Beautiful Soup enough?
Beautiful Soup is a very powerful library that makes web scraping by traversing the DOM (document object model) easier to implement. But it does only static scraping (ignores JavaScript). 

The combination of Beautiful Soup and Selenium will do the job of dynamic scraping. Selenium automates web browser interaction from python. Hence the data rendered by JavaScript links can be made available by automating the button clicks with Selenium and then can be extracted by Beautiful Soup.


Beautiful Soup is a very powerful library that makes web scraping by traversing the DOM (document object model) easier to implement. But it does only static scraping (ignores JavaScript). 

The combination of Beautiful Soup and Selenium will do the job of dynamic scraping. Selenium automates web browser interaction from python. Hence the data rendered by JavaScript links can be made available by automating the button clicks with Selenium and then can be extracted by Beautiful Soup.

Requirements :

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

This is the link to get chrome and firefox drivers :

Chromedriver : https://sites.google.com/a/chromium.org/chromedriver/downloads

Firefoxdriver : https://github.com/mozilla/geckodriver/releases



These are the two command to install Beautifulsoup and Selenium in your machine :

pip install selenium
sudo apt-get install python3-bs4
