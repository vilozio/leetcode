from dataclasses import dataclass
from typing import Dict


@dataclass
class CachedValue:
    key: int
    value: int
    next: 'CachedValue' = None
    prev: 'CachedValue' = None


class DLinkedList:
    def __init__(self):
        # Sentinel nodes.
        self.head: CachedValue = CachedValue(0, 0)
        self.tail: CachedValue = CachedValue(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def pop_head(self):
        x = self.head.next
        self.delete(x)
        return x

    def delete(self, x):
        x.prev.next, x.next.prev = x.next, x.prev
        x.prev, x.next = None, None  # Clear links.
        return x

    def append(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x

    def move_to_tail(self, x):
        self.delete(x)
        self.append(x)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table: Dict[int, CachedValue] = {}
        self.ages = DLinkedList()

    def get(self, key: int) -> int:
        cached = self.hash_table.get(key)
        if not cached:
            return -1
        self.ages.move_to_tail(cached)
        return cached.value

    def put(self, key: int, value: int) -> None:
        contains_key = key in self.hash_table
        if len(self.hash_table) == self.capacity and not contains_key:
            head = self.ages.pop_head()
            del self.hash_table[head.key]
        if contains_key:
            cached = self.ages.delete(self.hash_table[key])
            cached.value = value
        else:
            cached = CachedValue(key, value)
        self.hash_table[key] = cached
        self.ages.append(cached)


def testcase1():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1
    lru_cache.put(4, 4)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4


def testcase2():
    lru_cache = LRUCache(4)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    lru_cache.put(4, 4)
    lru_cache.put(5, 5)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(4) == 4
    lru_cache.put(6, 6)
    assert lru_cache.get(2) == -1


def testcase3():
    lru_cache = LRUCache(1)
    lru_cache.put(1, 1)
    assert lru_cache.get(1) == 1
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 2
    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1
    assert lru_cache.get(3) == 3


def testcase4():
    lru_cache = LRUCache(2)
    assert lru_cache.get(2) == -1
    lru_cache.put(2, 6)
    assert lru_cache.get(1) == -1
    lru_cache.put(1, 5)
    lru_cache.put(1, 2)
    assert lru_cache.get(1) == 2
    assert lru_cache.get(2) == 6


def testcase5():
    lru_cache = LRUCache(2)
    lru_cache.put(2, 1)
    lru_cache.put(1, 1)
    lru_cache.put(2, 3)
    lru_cache.put(4, 1)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 3


def test():
    testcase1()
    testcase2()
    testcase3()
    testcase4()
    testcase5()
