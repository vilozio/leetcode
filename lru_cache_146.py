from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class CachedValue:
    key: int
    value: int
    age: int
    next: 'CachedValue' = None
    prev: 'CachedValue' = None


class LinkedList:
    def __init__(self):
        self.head: Optional[CachedValue] = None
        self.tail: Optional[CachedValue] = None

    def delete_head(self):
        head = self.head
        if self.head:
            self.head = self.head.next
            head.next = None  # clean link
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev
        else:
            self.tail = x.prev

    def append(self, x):
        if self.tail:
            self.tail.next = x
        x.prev = self.tail
        self.tail = x
        if not self.head:
            self.head = x

    def move_to_tail(self, x):
        if self.tail == x:
            return
        if x.prev:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next:
            x.next.prev = x.prev
            x.next = None
        self.append(x)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table: Dict[int, CachedValue] = {}
        self.ages = LinkedList()

    def get(self, key: int) -> int:
        cached = self.hash_table.get(key)
        if not cached:
            return -1
        cached.age = self.ages.tail.age + 1
        self.ages.move_to_tail(cached)
        return cached.value

    def put(self, key: int, value: int) -> None:
        if len(self.hash_table) == self.capacity and key not in self.hash_table:
            del self.hash_table[self.ages.head.key]
            self.ages.delete_head()
        if key in self.hash_table:
            self.ages.delete(self.hash_table[key])
        age = self.ages.tail.age + 1 if self.ages.tail else 0
        cached = CachedValue(key, value, age)
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
