import falcon

from server.resources.user_tweets import UserTweets
from server.resources.search import SearchTweets


api = application = falcon.API()

api.add_route('/users/{user}', UserTweets())
api.add_route('/hashtags/{word}', SearchTweets())