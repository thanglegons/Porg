from time import sleep
import unittest
from cache.LRU_cache import LRUCache


class Test(unittest.TestCase):
    cache = LRUCache(5, 10)  # Maximum 5 items and 10 seconds to expire

    def test_insert_item(self):
        print("Test inserting items")
        try:
            self.assertTrue(self.cache.insert_item({5: 1}, 7))
            self.assertTrue(self.cache.insert_item({6: 2}, 8))
            self.assertTrue(self.cache.insert_item({1: 2}, 9))
            self.assertTrue(self.cache.insert_item({5: 2}, 10))
            self.assertTrue(self.cache.insert_item({12: 2}, 11))
            print("OK")
        except Exception:
            print("Something wrong")
            print(Exception)
            self.assertTrue(0)

    @staticmethod
    def print_cache(_cache):
        tail = _cache.tail
        head = _cache.head
        while tail is not head:
            print(tail.value)
            tail = tail.nxt
        if head is not None:
            print(head.value)

    @staticmethod
    def print_cache_rev(_cache):
        tail = _cache.tail
        head = _cache.head
        while tail is not head:
            print(head.value)
            head = head.prev
        if tail is not None:
            print(tail.value)

    def test_cache_works_forward(self):
        try:
            print("Test cache works")
            # insert cache first
            self.cache.insert_item({5: 1}, 7)
            self.cache.insert_item({3: 1}, 8)
            self.cache.insert_item({5: 2}, 1)
            Test.print_cache(self.cache)
            Test.print_cache_rev(self.cache)
            self.assertTrue(1)
            print("OK")
        except Exception:
            print("Something wrong")
            print(Exception)
            self.assertTrue(0)

    def test_get_item(self):
        try:
            print("Test get item")
            _cache = LRUCache(5, 10)
            _cache.insert_item({5: 1}, 7)
            _cache.insert_item({3: 1}, 8)
            _cache.insert_item({5: 2}, 1)
            self.assertEqual(_cache.get_item({5: 1}), 7)
            print("OK")
        except Exception:
            print("Something wrong")
            print(Exception)
            self.assertTrue(0)

    def test_time_expired(self):
        try:
            print("Test expired time works")
            _cache = LRUCache(5, 10)
            _cache.insert_item({5: 1}, 7)
            _cache.insert_item({3: 1}, 8)
            _cache.insert_item({5: 2}, 1)
            sleep(15)
            _cache.update_cache()
            self.assertEqual(_cache.get_item({5: 1}), None)
            self.assertEqual(_cache.get_item({3: 1}), None)
            print("OK")
        except Exception:
            print("Something wrong")
            print(Exception)
            self.assertTrue(0)


if __name__ == '__main__':
    unittest.main()
