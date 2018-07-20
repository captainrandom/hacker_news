"""HackerNews Datasource

api is documented here: https://github.com/HackerNews/API
"""
import requests


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
