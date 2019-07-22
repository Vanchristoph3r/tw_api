import json

import falcon
from voluptuous import Schema
from voluptuous.error import Error as ValidationError
from voluptuous.humanize import validate_with_humanized_errors
from scraper.twittersearch import TwitterSearch

class SearchTweets(object):

    validator = Schema({'limit': str}, required=False)
    default = 30

    def on_get(self, req, resp, word):
        """
            Return http response
            Get method for get tweets of word
        """
        data = req.params
        validate_with_humanized_errors(data, SearchTweets.validator)
        if 'limit' in data and data.get('limit', '').isdigit():
            limit = int(data.get('limit'))
        elif 'limit' in data and not data.get('limit', '').isdigit():
            raise falcon.HTTPBadRequest('Invalid parameter in endpoint')
        else:
            limit = self.default
        try:
            tweet_word = TwitterSearch(word)
            tweets = tweet_word.get_tweets(limit)
            resp.body = tweets
            resp.status = falcon.HTTP_200
        except Exception as error:
            resp.status = falcon.HTTP_404

