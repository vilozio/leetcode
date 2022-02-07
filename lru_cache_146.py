from dataclasses import dataclass
from typing import Dict, List


@dataclass
class CachedValue:
    key: int
    value: int
    age_pointer: int
    age: int = 0


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table: Dict[int, CachedValue] = {}
        self.age_order: List[CachedValue] = []
        self.age_first_entry = {0: 0}

    def swap_age_order(self, older: CachedValue, newer: CachedValue):
        newer_age_pointer = newer.age_pointer
        older.age_pointer, newer.age_pointer = newer.age_pointer, older.age_pointer
        swap(self.age_order, older.age_pointer, newer.age_pointer)
        self.age_first_entry[newer.age] = newer_age_pointer + 1
        if newer_age_pointer == 0:
            self.age_first_entry[older.age] = 0

    def get(self, key: int) -> int:
        cached_value = self.hash_table.get(key)
        if cached_value is None:
            return -1
        cached_value.age += 1
        if cached_value.age_pointer > 0:
            age_pointer = cached_value.age_pointer
            lower_age = self.age_order[age_pointer - 1]
            if cached_value.age > lower_age.age:
                lower_age_first_entry = self.age_first_entry[lower_age.age]
                self.swap_age_order(cached_value, self.age_order[lower_age_first_entry])
            elif cached_value.age == lower_age.age:
                if cached_value.age_pointer == len(self.age_order) - 1:
                    del self.age_first_entry[cached_value.age - 1]
                else:
                    self.age_first_entry[cached_value.age - 1] += 1
        else:
            self.age_first_entry[cached_value.age] = 0
            self.age_first_entry[cached_value.age - 1] += 1
        return cached_value.value

    def put(self, key: int, value: int) -> None:
        prev_cached: CachedValue = self.hash_table.get(key)
        if prev_cached:
            prev_cached.value = value
        else:
            cached_value = CachedValue(key, value, len(self.age_order))
            if len(self.age_order) == self.capacity:
                newest_age = self.age_order[-1].age
                newest_age_first_entry = self.age_first_entry[newest_age]
                del self.hash_table[self.age_order[newest_age_first_entry].key]
                if newest_age_first_entry != len(self.age_order) - 1:
                    for i in range(newest_age_first_entry + 1, len(self.age_order)):
                        self.age_order[i].age_pointer = i - 1
                        self.age_order[i - 1] = self.age_order[i]
                cached_value.age_pointer -= 1
                self.age_order[-1] = cached_value
            else:
                self.age_order.append(cached_value)
            self.hash_table[key] = cached_value


def testcase1():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1
    lru_cache.put(4, 4)
    assert lru_cache.get(1) == 1
    assert lru_cache.get(3) == -1
    assert lru_cache.get(4) == 4


def testcase2():
    lru_cache = LRUCache(3)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    lru_cache.get(3)
    assert lru_cache.age_order[0].value == 3
    lru_cache.get(2)
    assert lru_cache.age_order[1].value == 2
    lru_cache.put(4, 4)
    assert 1 not in lru_cache.hash_table


def test():
    testcase1()
    testcase2()
