from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev_nums = set()
        for num in nums:
            if num in prev_nums:
                return True
            prev_nums.add(num)
        return False
