from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for i in range(1, len(set_nums) + 1):
            if i not in set_nums:
                return i
        return len(set_nums) + 1
