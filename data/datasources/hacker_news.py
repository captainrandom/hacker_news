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
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/item/{}.json'.format(id)
        )
        return response.json()
       # return response.json()
    def get_top_stories(self):
        """Fetches and returns top stories."""
        raise NotImplementedError()


class HackerNewsItem(Item):
    """Represents a HackerNews Item."""

    def get_name(self):
        return self.data

    def get_description(self):
        return  self.data

    # def get_url(self):
    #     return self.data.get('url', '')


class HackerNewsItems(Items):
    """Represent trending stories from HackerNews."""
    item_cls = HackerNewsItem

    def get_data(self):
        story = []
        hackernews_datasource = HackerNewsDatasource()
        response_json = hackernews_datasource.get_topstory_ids()
        for ids in response_json[0:10]:
            response_json = hackernews_datasource.get_story(ids) 
            story.append(response_json)
        # return 'title: {}\nurl:{}'.format(response_json['title'],response_json['url'])
        return story
