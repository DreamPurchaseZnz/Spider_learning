"""
Writen by Ethan
Spider for dynamic web using selenium
Add a new terminal term -> the page height limitation
"""

from selenium import webdriver
import time
import re
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    executable_path=r"C:\Program Files\Anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver_win33\chromedriver.exe"
)

url = "http://nbacp.com/"
driver.get(url)
SCROLL_PAUSE_TIME = 2

#  Number of pages
page = 0
page_num = 10000
last_height = driver.execute_script("return document.body.scrollHeight")

while page <= page_num:
    # scroll down to the bottom
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    page += 1

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

htmlSource = driver.page_source
f = open("wanghongpaipai.txt", "w", encoding="utf8")
f.write(htmlSource)
f.close()


# Get more details by filtering the useful information
def getDetails(tag):
    prop = {}
    prop["title"] = re.findall(
        r'(?<=<div class="title">)(.+)</div><div', str(tag))[0]
    prop["type"] = re.findall(
        r'(?<=<div class="meta">)#(\S+) / \S+</div></div>', str(tag))[0]
    prop["property"] = re.findall(
        r'(?<=<div class="meta">)#\S+ / (\S+)</div></div>', str(tag))[0]
    vid = re.findall(
        r'(?<=<div class="video" data-vid=)(\S+) progid:', str(tag))[0]
    prop["url"] = "http://nbacp.com/free/detail?vid=%s"%vid.replace('"', '')
    return prop

# unpack the file of wanghongpaipai.txt
htmlSource = open("wanghongpaipai.txt", encoding="utf8")
soup = BeautifulSoup(htmlSource, "lxml")
dataList = []
for tag in soup.find_all("div", class_="video"):
    data = getDetails(tag)
    dataList.append(data)

my_df = pd.DataFrame(dataList)
my_df.to_csv("WHMore.csv")



