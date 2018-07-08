"""HackerNews Datasource

api is documented here: https://github.com/HackerNews/API
"""
import requests
from data.base import Item, Items

class HackerNewsDatasource(object):
    """Handles all communication with HackerNews"""

    def get_topstory_ids(self):
        """Returns a list of current top story ids."""
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/topstories.json')
        return response.json()

    def get_story(self, id):
        """Fetches and returns a story."""
        raise NotImplementedError()

    def get_top_stories(self):
        """Fetches and returns top stories."""
        raise NotImplementedError()


class HackerNewsItem(Item):
    """Represents a Giphy Item."""

    def get_name(self):
        print self.data

    # def get_description(self):
    #     return 'rating: {} imported: {}'.format(
    #         self.data.get('rating', 'n/a'),
    #         self.data.get('import_datetime', ''))

    # def get_url(self):
    #     return self.data.get('url', '')


class HackerNewsItems(Items):
    """Represent trending gifs from Giphy."""
    item_cls = HackerNewsItem

    def get_data(self):
        hackernews_datasource = HackerNewsDatasource()
        response_json = hackernews_datasource.get_topstory_ids()
        return response_json
