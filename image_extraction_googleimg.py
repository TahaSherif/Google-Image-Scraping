import urllib.request #import urllib.request
from bs4 import BeautifulSoup #import BeautifulSoup
from selenium import webdriver #import webdriver
from selenium.webdriver.common.keys import Keys #import Keys
import time #import time; enablues you to use .sleep() while crwaling imges

# instantiate browser
binary = r'/home/taha/Documents/chromedriver_linux64/chromedriver' #path to the chrome driver
browser = webdriver.Chrome(binary) #init browser

#get browser. this will open a new ready-for-searching tab of Chrome browser
browser.get("https://www.google.com/imghp?hl=en&search?hl=en&q=") 

elem = browser.find_element_by_name("q") #init elem
elem.send_keys("dog") #keywords that you wanna use to search
time.sleep(3)
elem.submit() #elem.submit()

# for-loop 
for i in range(1 ,6):
    # find body tag and execute send_keys(Keys.END) for i < 10 so 9 times
    # Keys.END is when the END key is executed to be clicked
    browser.find_element_by_xpath("//body").send_keys(Keys.END)  #smb == when clicking show more result button
    try:
        browser.find_element_by_id("smb").click()
        time.sleep(5)
    except:
        time.sleep(5)
time.sleep(5)

html = browser.page_source # get page_source from browser

# init soup by calling the method BeautifulSoup with the parameters; the variable html and "html.parser"
soup = BeautifulSoup(html, "html.parser") #this code enables you to fetch the image urls and download the images

# method for listing url
def fetch_list_url():
    params = [] #declare and init an array

    # find all img tags and the class whose name is rg_i
    imgList = soup.find_all("img", class_ ="rg_i")

    #Now, extract the img sources(urls) from imgList
    for im in imgList:
        try:
            params.append(im["src"]) #source address of an img in the class rg_i
        except KeyError:
            params.append(im["data-src"])
    return params #return params`

# method for downloading imgs from the url
def fetch_detail_url():
    params = fetch_list_url() #init params by calling the method fetch_list_url()

    # print(params)
    a = 1 #a = 1
    for p in params:
        # @param p. the source img urls in params are assigned into p with this foreach-loop if urls are fetched properly   
        # @param path; gives download path
        # @param a; gives auto-incrementing numeric file name
        # finally, set .jpg extension to each of the img downloaded.
        urllib.request.urlretrieve(p, r"/home/taha/Documents/google_images/image"+ str(a) + ".jpeg" )
        a+=1 #a = a + 1; increment nums

#by calling the method fetch_detail_url(), the method fetch_list_url() is executed first in it.
fetch_detail_url() #fetch_detail_url()
browser.quit() #close the browser