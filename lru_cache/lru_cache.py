import collections


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.limit:
                self.cache.popitem(last=False)
        self.cache[key] = value
