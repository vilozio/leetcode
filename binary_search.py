from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1


def call(nums, target):
    s = Solution()
    return s.search(nums, target)


def test():
    assert call([-1, 0, 3, 5, 9, 12], 9) == 4
    assert call([-1, 0, 3, 5, 9, 12], 2) == -1
    assert call([], 2) == -1
    assert call([1], 1) == 0
