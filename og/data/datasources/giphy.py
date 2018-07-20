"""Giphy.com Datasource

api is documented here: https://github.com/Giphy/GiphyAPI
"""
import requests
from data.base import Item, Items


class GiphyDatasource(object):
    """Handles all communication with Giphy"""

    def get_trending_gifs(self):
        """Returns a list of trending gifs."""
        response = requests.get('http://api.giphy.com/v1/gifs/trending',
                                params={'api_key': 'dc6zaTOxFJmzC'})
        return response.json()


class GiphyItem(Item):
    """Represents a Giphy Item."""

    def get_name(self):
        return self.data.get('slug', '')

    def get_description(self):
        return 'rating: {} imported: {}'.format(
            self.data.get('rating', 'n/a'),
            self.data.get('import_datetime', ''))

    def get_url(self):
        return self.data.get('url', '')


class GiphyItems(Items):
    """Represent trending gifs from Giphy."""
    item_cls = GiphyItem

    def get_data(self):
        giphy_datasource = GiphyDatasource()
        response_json = giphy_datasource.get_trending_gifs()
        return response_json['data']
