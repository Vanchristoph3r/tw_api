"""
python3.6
ipython console test
"""
import selenium

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
# from webdriver_manager.chrome import ChromeDriverManager

# self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=options)

driver.get('https://twitter.com/eleseguey')

loopCounter = 0
lastHeight = driver.execute_script("return document.body.scrollHeight")
import pdb; pdb.set_trace()

_selector = Selector(text = driver.page_source)
# url = _selector.css('h1.ProfileHeaderCard-name').xpath('//a[has-class("ProfileHeaderCard-nameLink")]').attrib['href']
# name = _selector.css('h1.ProfileHeaderCard-name').xpath('//a[has-class("ProfileHeaderCard-nameLink")]/text()').extract()


user_id = _selector.css('div.user-actions').attrib['data-user-id']
#'7643702'
username = _selector.css('div.user-actions').attrib['data-screen-name']
#'eleseguey'
name = _selector.css('div.user-actions').attrib['data-name']
#'Gio'
private = _selector.css('div.user-actions').attrib['data-protected']
#'false'

# _selector.css('div.ProfileTimeline .stream-container .stream')
# ttt=[x for x in _selector.css('div.ProfileTimeline .stream-container .stream').xpath('//ol[@id="stream-items-id"]/li')]
tweets = _selector.css('div.ProfileTimeline .stream-container .stream').xpath('//ol[@id="stream-items-id"]/li')
for tweet in tweets:
	pass
while True:
    if loopCounter > 50:
        break; # if the account follows a ton of people, its probably a bot, cut it off
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
    loopCounter = loopCounter + 1

scrapy_selector = Selector(text = driver.page_source)
scrapy_selector.css('div.content').xpath('//p[has-class("tweet-text")]/text()').extract()

import pdb; pdb.set_trace()