from cache.LRU_cache import LRUCache


class SearchCache(object):
    cache = LRUCache(5, 5 * 60)
