from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if (n2_idx := d.get(n)) is not None:
                return [n2_idx, i]
            d[target - n] = i
        return []


def call(nums, target):
    s = Solution()
    return s.twoSum(nums, target)


def test():
    assert call([2, 7, 11, 15], 9) == [0, 1]
    assert call([], 9) == []
    assert call([3, 2, 4], 6) == [1, 2]
    assert call([3, 3], 6) == [0, 1]
    assert call([3, 1, 1, 1, 1, 3], 6) == [0, 5]
    assert call([3, 1, 1, 3, 1, 3], 6) == [0, 3]
    assert call([2, 1, 1, 2, 1, 3], 5) == [3, 5]
