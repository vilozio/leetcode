from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


def call(intervals):
    s = Solution()
    return s.merge(intervals)


def test():
    assert call([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert call([[100, 200], [1, 5], [4, 7], [10, 20], [15, 101], [250, 260], [199, 250]]) == [
        [1, 7], [10, 260]
    ]
    assert call([[1, 5], [4, 7], [10, 20], [100, 200], [15, 101], [250, 260], [199, 250]]) == [
        [1, 7], [10, 260]
    ]
    assert call([[1, 5], [4, 7], [10, 20], [100, 200], [15, 101], [250, 260], [199, 250], [350, 350], [261, 350],
                 [350, 400]]) == [
               [1, 7], [10, 260], [261, 400]
           ]
    assert call([[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]) == [[0, 0], [1, 1], [2, 6]]
    assert call([[5, 5], [1, 3], [3, 5], [4, 6], [1, 1], [3, 3], [5, 6], [3, 3], [2, 4], [0, 0]]) == [[0, 0], [1, 6]]
    assert call([[5, 5], [1, 2], [2, 4], [2, 3], [4, 4], [5, 5], [2, 3], [5, 6], [0, 0], [5, 6]]) == [
        [0, 0], [1, 4], [5, 6]
    ]
    assert call([[3, 3], [1, 1], [0, 2], [2, 2], [1, 2], [1, 3], [1, 1], [3, 3], [2, 3], [4, 6]]) == [
        [0, 3], [4, 6]
    ]
