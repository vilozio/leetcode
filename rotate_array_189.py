from typing import List


class Solution:
    def swap(self, nums, from_indices, to_indices):
        i, j = from_indices[0], to_indices[0]
        while i <= from_indices[1] and j <= to_indices[1]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    def rotate(self, nums: List[int], k: int, from_i=0, to_i=None, to_right=True) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        if to_i is None:
            to_i = len(nums) - 1
        n = to_i - from_i + 1
        if n // 2 >= k:
            for i in range(n // k):
                if to_right:
                    from_indices = (from_i + i * k, from_i + i * k + k - 1)
                    to_indices = (to_i - k + 1, to_i)
                    if from_indices[1] >= to_indices[0]:
                        from_indices = (from_indices[0], to_indices[0] - 1)
                else:
                    from_indices = (from_i, from_i + k - 1)
                    to_indices = (to_i - i * k - k + 1, to_i - i * k)
                    if from_indices[1] >= to_indices[0]:
                        to_indices = (from_indices[1] + 1, to_indices[1])
                len_from = from_indices[1] - from_indices[0] + 1
                len_to = to_indices[1] - to_indices[0] + 1
                if len_from == len_to:
                    self.swap(nums, from_indices, to_indices)
                else:
                    self.rotate(nums, len_from if to_right else len_to,
                                min(from_indices[0], to_indices[0]),
                                max(from_indices[1], to_indices[1]), not to_right)
        elif k < n:
            self.rotate(nums, n - k, from_i, to_i, not to_right)
        else:
            self.rotate(nums, k % n, from_i, to_i, to_right)


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
