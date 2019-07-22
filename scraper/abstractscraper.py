import selenium
import json 
import re

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from .settings import DRIVER_PATH, URI_TWITTER


class AbstractScraper:
    """Abstract class for Scraper Driver"""
    def create_driver(self) -> 'webdriver':
        """
            Return webdriver object
            Create webdriver to scrap
        """
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)

        return driver

    def _extract_info(self, selector: 'Selector', old_tweets: list) -> list:
        """
            Returns two lists
            Extract info of each tweet on the stream
        """
        tweets_arr = []
        tweets = selector.css('div.stream').xpath('.//ol[@id="stream-items-id"]')       
        for tweet in tweets.xpath('.//li[has-class("stream-item")]'):
            user_info = tweet.xpath('.//div[has-class("stream-item-header")]').xpath('.//a[has-class("account-group")]')
            user_username = user_info.attrib['href']
            user_name = user_info.xpath('.//span[has-class("username")]/b/text()').get()
            user_id = user_info.attrib['data-user-id']
            date = tweet.xpath('.//a[has-class("tweet-timestamp")]').attrib['title']
            if date in old_tweets:
                continue
            text = tweet.xpath('.//p[has-class("tweet-text")]/text()').get()
            if not text:
                text = tweet.xpath('.//div[has-class("js-adaptive-photo")]').attrib['data-image-url']
            reply = tweet.xpath('.//div[has-class("ProfileTweet-action--reply")]').xpath('.//span[has-class("ProfileTweet-actionCountForPresentation")]/text()').get()
            rt = tweet.xpath('.//div[has-class("ProfileTweet-action--retweet")]').xpath('.//span[has-class("ProfileTweet-actionCountForPresentation")]/text()').get()
            fav = tweet.xpath('.//div[has-class("ProfileTweet-action--favorite")]').xpath('.//span[has-class("ProfileTweet-actionCountForPresentation")]/text()').get()
            hashtags = []
            for hashtag in tweet.xpath('.//a[has-class("twitter-hashtag")]'):
                hashtags.append(hashtag.xpath('.//b/text()').get())
            tweet_info = {'account':{"username": user_username, "name": user_name, "user_id": user_id},
                          'date':date, 'text': text,
                          'reply':reply, 'retweets':rt,
                          'favorite':fav, 'hashtags': hashtags}
            tweets_arr.append(tweet_info)
            old_tweets.append(date+user_id)

        return tweets_arr, old_tweets

    def collect_tweets(self, query: str, limit: int) -> 'json':
        """
            Return json
            Collect a limit of tweets looping through the stream 
        """
        driver = self.create_driver()
        driver.get(URI_TWITTER.format(query))
        selector = Selector(text = driver.page_source)
        loop_counter = 0
        old_tweets = []
        tweets_arr, old_tweets = self._extract_info(selector, old_tweets)
        loop_counter = len(tweets_arr)

        if loop_counter <= limit:
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                if loop_counter > 50:
                    break;
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break

                new_selector = Selector(text=driver.page_source)
                tweets_arr_aux, old_tweets_uax = self._extract_info(new_selector, old_tweets)
                tweets_arr += tweets_arr_aux
                old_tweets += old_tweets_uax
                last_height = new_height
                loop_counter = len(tweets_arr)
        driver.quit()
        tweets_arr = tweets_arr[:limit]
        tweets_json = json.dumps(tweets_arr)
        return tweets_json
