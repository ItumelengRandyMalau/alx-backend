#!/usr/bin/python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """  """

    def __init__(self):
        """ initializes the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """  discards the most recently used item in the """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discardedItem = self.order.pop()
            del self.cache_data[discardedItem]
            print("DISCARD: {}".format(discardedItem))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Returns the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
