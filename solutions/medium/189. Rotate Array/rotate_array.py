from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1


def testcase(nums, k, result):
    s = Solution()
    s.rotate(nums, k)
    assert nums == result


def test():
    testcase([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
    testcase([-1, -100, 3, 99], 2, [3, 99, -1, -100])
    testcase([-1, -100, 3, 99], 0, [-1, -100, 3, 99])
    testcase([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [7, 8, 9, 1, 2, 3, 4, 5, 6])
    testcase([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [8, 9, 1, 2, 3, 4, 5, 6, 7])
    testcase([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [6, 7, 8, 9, 1, 2, 3, 4, 5])
    testcase([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [5, 6, 7, 8, 9, 1, 2, 3, 4])
    testcase([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15], 4, [11, 12, 13, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    testcase([1, 2, 3, 4, 5, 6, 7], 6, [2, 3, 4, 5, 6, 7, 1])
    testcase([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7])
    testcase([1, 2, 3, 4, 5, 6, 7], 14, [1, 2, 3, 4, 5, 6, 7])
    testcase([1, 2, 3, 4, 5, 6, 7], 15, [7, 1, 2, 3, 4, 5, 6])
    testcase([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 38,
             [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
