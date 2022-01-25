from typing import List


class Solution:
    def swap(self, nums, from_indices, to_indices, to_right):
        len_from = from_indices[1] - from_indices[0]
        len_to = to_indices[1] - to_indices[0]
        if len_from == len_to:
            i, j = from_indices[0], to_indices[0]
            while i <= from_indices[1] and j <= to_indices[1]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        else:
            self.rotate(nums, len_to,
                        min(from_indices[0], to_indices[0]),
                        max(from_indices[1], to_indices[1]) + 1, not to_right)

    def rotate(self, nums: List[int], k: int, from_i=0, to_i=None, to_right=True) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if to_i is None:
            to_i = len(nums)
        n = to_i - from_i
        if n // 2 >= k:
            for i in range((n // k - 1) + n % k):
                if to_right:
                    from_indices = (i * k, i * k + k - 1)
                    to_indices = (n - k, n - 1)
                    if from_indices[1] >= to_indices[0]:
                        from_indices = (from_indices[0], to_indices[0] - 1)
                else:
                    from_indices = (from_i, from_i + k - 1)
                    to_indices = (n - i * k - k, n - i * k - 1)
                    if from_indices[1] >= to_indices[0]:
                        to_indices = (from_indices[1] + 1, to_indices[0])
                self.swap(nums, from_indices, to_indices, to_right)
        else:
            self.rotate(nums, n - k, from_i, to_i, not to_right)


def testcase(nums, k, result):
    s = Solution()
    s.rotate(nums, k)
    assert nums == result


def test():
    testcase([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
