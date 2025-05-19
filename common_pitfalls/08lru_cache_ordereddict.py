from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=3):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)
cache.put(1, 'A')
cache.put(2, 'B')
print(cache.get(1))  # Output: A
cache.put(3, 'C')
print(cache.get(2))  # Output: -1 (evicted)
