"""Base classes for Data representations."""


class Items(object):
    """Represents a list of Data Items."""
    item_cls = None

    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        """Returns a list of data from thrid party."""
        raise NotImplementedError()

    def print_rows(self):
        for item_data in self.data:
            item = self.item_cls(item_data)
            item.print_row()


class Item(object):
    """Represent a Data item form thrid parties."""

    def __init__(self, data):
        self.data = data
        self.name = self.get_name()
        self.description = self.get_description()
        self.url = self.get_url()

    def get_name(self):
        """Returns a Name for item."""
        raise NotImplementedError()

    def get_description(self):
        """Returns a desciption of the item."""
        raise NotImplementedError()

    def get_url(self):
        """Return URL for the item."""
        raise NotImplementedError()

    def print_row(self):
        print('{name:30.30}|{description:50.50}|{url}'.format(
            name=self.name, description=self.description, url=self.url))
