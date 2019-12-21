from cache.LRU_cache import LRUCache


class RecommendCache(object):
    cache = LRUCache(1024, 5 * 60)
