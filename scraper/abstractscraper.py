import selenium

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from settings import DRIVER_PATH


class AbstractScraper:
    """Abstract class for Scraper Driver"""
    def create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)
        return driver


