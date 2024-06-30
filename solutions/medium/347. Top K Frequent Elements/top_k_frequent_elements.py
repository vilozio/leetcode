from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ordered = defaultdict(list)
        for num, num_freq in freq.items():
            ordered[num_freq].append(num)

        ordered_keys = reversed(sorted(ordered.keys()))
        result = []
        for key in ordered_keys:
            for num in ordered[key]:
                if len(result) < k:
                    result.append(num)
                else:
                    return result
        return result
