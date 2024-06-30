from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# 1, 2, 4, 5, 6, 8

# 1 : 2, 2: 2, 4: 3, 5: 3, 6: 3
# 100: 1, 4: 1, 200: 1, 1: 1, 3: 1, 2: 2
