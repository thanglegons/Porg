from time import sleep

from cache.LRU_cache import LRUCache

cache = LRUCache(5, 10)

cache.insert_item({5: 1}, 7)
cache.insert_item({6: 2}, 8)
cache.insert_item({1: 2}, 9)
cache.insert_item({5: 2}, 10)
cache.insert_item({12: 2}, 11)


def print_cache(cache):
    tail = cache.tail
    head = cache.head
    while tail is not head:
        print(tail.value)
        tail = tail.nxt
    if head is not None:
        print(head.value)


def print_cache_rev(cache):
    tail = cache.tail
    head = cache.head
    while tail is not head:
        print(head.value)
        head = head.prev
    if tail is not None:
        print(tail.value)


print_cache(cache)
print('------')
# print_cache_rev(cache)
cache.insert_item({13: 2}, 13)
cache.insert_item({13: 5}, 15)
# print(cache.get_item({5: 1}).value)
# cache.get_item({})
print('------')
cache.get_item({5: 2})
print_cache(cache)
print('------')
# print_cache_rev(cache)
