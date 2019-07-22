import selenium
import json 

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from scrapy.http import Request
from .abstractscraper import AbstractScraper
from .settings import URI_TWITTER



class TwitterSearch(AbstractScraper):
    """Class for search scraper"""
    def __init__(self, word):
        super(TwitterSearch, self).__init__()
        self.word = word

    def get_tweets(self, limit: int) -> str:
        """Return a string json
            Method to get tweets of User
        """
        query='search?q='+self.word
        tweets = self.collect_tweets(query, limit)
        return tweets
        