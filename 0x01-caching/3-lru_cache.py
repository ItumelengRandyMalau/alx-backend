#!/usr/bin/python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUcache class

    Args: BaseCaching module
    """
    def __init__(self):
        """ Intiates the LRUCache class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """  discards the least recently used item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            """ moves the key to the end of the list """
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Gets item by key """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
