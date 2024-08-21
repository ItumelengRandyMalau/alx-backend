#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ Adds an item in the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Gets an item by key """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
