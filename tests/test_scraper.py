from scraper.twitteruser import TwitterUser
from scraper.twittersearch import TwitterSearch
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
import pytest
import os 

# os.environ['DRIVER_PATH'] = os.getenv('DRIVER_PATH', '/usr/local/bin/chromedriver')

def test_create_obj():
    obj = TwitterUser('asf')
    assert type(obj) == TwitterUser

def test_is_private():
    obj = TwitterUser('gio90111')
    with pytest.raises(ValueError):
        obj._is_private()

def test_get_tweets_error_limit():
    obj = TwitterUser('asf')
    with pytest.raises(TypeError):
        obj.get_tweets()

def test_get_tweets():
    obj = TwitterUser('asf')
    assert type(obj.get_tweets(10)) == str

def test_collect_tweets_error():
    obj = TwitterUser('asf')
    with pytest.raises(TypeError):
        obj.collect_tweets()

def test_collect_tweets():
    obj = TwitterUser('asf')
    assert type(obj.collect_tweets(obj.username, 10)) == str

def test_create_driver():
    obj = TwitterUser('asf')
    driver = obj.create_driver()
    driver.quit()

    assert isinstance(driver, WebDriver)

def test_get_tweets_search():
    obj = TwitterSearch('dogs')
    assert type(obj.get_tweets(1)) == str

def test_get_tweets_error_limit():
    obj = TwitterSearch(10)
    with pytest.raises(TypeError):
        obj.get_tweets()

def test_web_drive_fail():
    os.environ['DRIVER_PATH'] = '/'
    obj = TwitterUser('asf')
    assert obj.create_driver()
