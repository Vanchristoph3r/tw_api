import selenium

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from scrapy.http import Request
from .abstractscraper import AbstractScraper
from .settings import URI_TWITTER


class TwitterUser(AbstractScraper):
    """Class for twitter user scraper"""
    def __init__(self, username):
        super(TwitterUser, self).__init__()
        self.username = username

    def _is_private(self):
        """
            Raise Error
            Method to validate if user is not private
        """
        driver = self.create_driver()
        driver.get(URI_TWITTER.format(self.username))
        selector = Selector(text = driver.page_source)
        private = selector.css('div.user-actions').attrib['data-protected']
        driver.quit()
        if private != 'false':
            raise ValueError('The user is private')

    def get_tweets(self, limit: int) -> str:
        """Return a string json
            Method to get tweets of User
        """
        self._is_private()
        tweets = self.collect_tweets(self.username, limit)
        return tweets
        