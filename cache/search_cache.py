from cache.LRU_cache import LRUCache


class SearchCache(object):
    cache = LRUCache(1024, 5 * 60)
