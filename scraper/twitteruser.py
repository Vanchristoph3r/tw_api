import selenium

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from scrapy.http import Request
from .abstraactscraper import AbstractScraper
from .settings import URI_TWITTER
# driver.quit()



class TwitterUser(AbstractScraper):
    """User object for twitter scraper"""
    def __init__(self, username):
        super(TwitterUser, self).__init__()
        self.username = username
        self.user_id = 0
        self.name = ''

    def _get_info(self, selector):
        private = selector.css('div.user-actions').attrib['data-protected']
        if private == 'false':
            return 'User is private'
        self.user_id = selector.css('div.user-actions').attrib['data-user-id']
        self.name = selector.css('div.user-actions').attrib['data-name']

    def get_tweets(self, limit):
        driver = self.get_driver()
        driver.get(URI_TWITTER.format(self.username))
        selector = Selector(text = driver.page_source)
        self._get_info(selector)
        
        loop_counter=0
        tweets_arr = []

        tweets = selector.css('div.stream').xpath('.//ol[@id="stream-items-id"]')
        for tweet in tweets.xpath('.//li[has-class("stream-item")]'):
            date = tweet.xpath('.//a[has-class("tweet-timestamp")]').attrib['title']
            text = tweet.xpath('.//p[has-class("tweet-text")]/text()').get()
            if not text:
                text = tweet.xpath('.//div[has-class("js-adaptive-photo")]').attrib['data-image-url']
            reply = tweet.xpath('.//div[has-class("ProfileTweet-action--reply")]').xpath('.//span[has-class("ProfileTweet-actionCountForPresentation")]/text()').get()
            rt = tweet.xpath('.//div[has-class("ProfileTweet-action--retweet")]').xpath('.//span[has-class("ProfileTweet-actionCountForPresentation")]/text()').get()
            fav = tweet.xpath('.//div[has-class("ProfileTweet-action--favorite")]').xpath('.//span[has-class("ProfileTweet-actionCountForPresentation")]/text()').get()
            tweet_info = {'date':date, 'text': text, 'reply':reply, 'retweets':rt, 'favorite':fav}
            tweets_arr.append(tweet_info)

        loop_counter = len(loop_counter)
        if len(tweets) <= limit:
            while True:
                if loop_counter > limit:
                    break;





        