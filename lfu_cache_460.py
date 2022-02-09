from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class CachedValue:
    key: int
    value: int
    next: 'CachedValue' = None
    prev: 'CachedValue' = None
    parent: 'ConnectedDLinkedList' = None


class ConnectedDLinkedList:
    def __init__(self, num: int, parent=None):
        # Sentinel nodes.
        self.head: CachedValue = CachedValue(0, 0)
        self.tail: CachedValue = CachedValue(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.next: Optional[ConnectedDLinkedList] = None
        self.prev: Optional[ConnectedDLinkedList] = None
        self.num = num
        self.parent = parent

    def pop_head(self) -> CachedValue:
        x = self.head.next
        self.delete(x)
        self.am_i_needed()
        return x

    def delete(self, x: CachedValue):
        x.prev.next, x.next.prev = x.next, x.prev
        x.prev, x.next = None, None  #
        x.parent = None              # Clear links.
        return x

    def am_i_needed(self):
        if self.head.next == self.tail:
            self.parent.delete(self)

    def append(self, x: CachedValue):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        x.parent = self

    def move_to_next(self, x: CachedValue):
        self.delete(x)
        self.parent.insert_after(self)
        self.next.append(x)
        self.am_i_needed()


class NestedDLinkedList:
    def __init__(self):
        self.head = ConnectedDLinkedList(0, parent=self)
        self.tail = ConnectedDLinkedList(0, parent=self)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, x: ConnectedDLinkedList):
        if x.num + 1 != x.next.num:
            new_next = ConnectedDLinkedList(x.num + 1, parent=self)
            new_next.next = x.next
            new_next.prev = x
            x.next.prev = new_next
            x.next = new_next

    def delete(self, x: ConnectedDLinkedList):
        x.prev.next, x.next.prev = x.next, x.prev
        x.prev, x.next = None, None  # Clear links.
        x.parent = None

    def pop_head(self) -> CachedValue:
        x = self.head.next.pop_head()
        return x

    def insert(self, x: CachedValue):
        self.insert_after(self.head)
        self.head.next.append(x)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table: Dict[int, CachedValue] = {}
        self.ages = NestedDLinkedList()

    def get(self, key: int) -> int:
        cached = self.hash_table.get(key)
        if not cached:
            return -1
        cached.parent.move_to_next(cached)
        # self.ages.move_to_tail(cached)
        return cached.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        contains_key = key in self.hash_table
        if len(self.hash_table) == self.capacity and not contains_key:
            head = self.ages.pop_head()
            del self.hash_table[head.key]
        if contains_key:
            cached = self.hash_table[key]
            cached.parent.move_to_next(cached)
            # cached = cached.parent.delete(cached)
            cached.value = value
        else:
            cached = CachedValue(key, value)
            self.ages.insert(cached)
        self.hash_table[key] = cached


def testcase1():
    lfu_cache = LFUCache(2)
    lfu_cache.put(1, 1)
    lfu_cache.put(2, 2)
    assert lfu_cache.get(1) == 1
    lfu_cache.put(3, 3)
    assert lfu_cache.get(2) == -1
    lfu_cache.put(4, 4)
    assert lfu_cache.get(1) == 1
    assert lfu_cache.get(3) == -1
    assert lfu_cache.get(4) == 4


def testcase2():
    lfu_cache = LFUCache(2)
    lfu_cache.put(1, 1)
    lfu_cache.put(2, 2)
    assert lfu_cache.get(1) == 1
    lfu_cache.put(3, 3)
    assert lfu_cache.get(2) == -1
    lfu_cache.put(4, 4)
    assert lfu_cache.get(1) == 1
    assert lfu_cache.get(3) == -1
    assert lfu_cache.get(4) == 4
    assert lfu_cache.get(4) == 4
    lfu_cache.put(5, 5)
    assert lfu_cache.get(1) == -1
    assert lfu_cache.get(4) == 4
    assert lfu_cache.get(5) == 5


def testcase3():
    lfu_cache = LFUCache(2)
    lfu_cache.put(1, 1)
    lfu_cache.put(2, 2)
    assert lfu_cache.get(1) == 1
    lfu_cache.put(3, 3)
    assert lfu_cache.get(2) == -1
    assert lfu_cache.get(3) == 3
    lfu_cache.put(4, 4)
    assert lfu_cache.get(1) == -1
    assert lfu_cache.get(3) == 3
    assert lfu_cache.get(4) == 4


def testcase4():
    lfu_cache = LFUCache(2)
    lfu_cache.put(1, 1)
    lfu_cache.put(1, 11)
    lfu_cache.put(2, 2)
    lfu_cache.put(3, 3)
    assert lfu_cache.get(1) == 11
    assert lfu_cache.get(2) == -1


def testcase5():
    lfu_cache = LFUCache(0)
    lfu_cache.put(0, 0)
    assert lfu_cache.get(0) == -1


def test():
    testcase1()
    testcase2()
    testcase3()
    testcase4()
    testcase5()
