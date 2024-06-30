from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        x_s = {}
        for x in nums:
            x_s[x] = x_s[x] + 1 if x in x_s else 1
        for i, y in enumerate(nums):
            for z in nums[i + 1:]:
                x = -y - z
                req_duplicates = int(x == y) + int(x == z)
                if x in x_s and x_s[x] > req_duplicates:
                    triplet = [x, y, z]
                    triplet.sort()
                    triplet = tuple(triplet)
                    triplets.add(triplet)
        return [list(t) for t in triplets]


def call(nums):
    s = Solution()
    return s.threeSum(nums)


def test():
    assert call([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert call([]) == []
    assert call([0]) == []
    assert call([-1, 0, 1, 2, -1, -4, 0, 9, 6, -9, -2]) == [[-1, 0, 1], [-1, -1, 2], [-4, -2, 6], [-9, 0, 9], [-2, 0, 2]]
