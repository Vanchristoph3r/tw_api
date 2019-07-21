import json

import falcon
from voluptuous import Schema
from voluptuous.error import Error as ValidationError
from voluptuous.humanize import validate_with_humanized_errors
from scraper.twitteruser import TwitterUser

class UserTweets(object):

	validator = Schema({'limit': int}, required=False)

	def on_get(self, req, resp, user):
        data = TwitterUser.get.params

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)
        validate_with_humanized_errors(data, S3Signature.validator)
        limit = data.get('limit') if 'limit' in data else 30

        tweet_user = TwitterUser(user)
        tweets = tweet_user.get_tweets(limit)
        resp.status = falcon.HTTP_200

