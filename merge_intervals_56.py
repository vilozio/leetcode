from typing import List


def bin_search(intervals: List[List[int]], num: int, interval_point: int, default_idx: int):
    left = 0
    insert_idx = default_idx
    right = len(intervals) - 1
    while left <= right:
        mid = (right + left) // 2
        if num < intervals[mid][interval_point]:
            insert_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    return insert_idx


def bin_search2(intervals: List[List[int]], num: int, interval_point: int, default_idx: int):
    left = 0
    insert_idx = default_idx
    right = len(intervals) - 1
    while left <= right:
        mid = (right + left) // 2
        if num < intervals[mid][interval_point]:
            right = mid - 1
        else:
            insert_idx = mid
            left = mid + 1
    return insert_idx


def create_extremum(intervals: List[List[int]]):
    extremum = []
    if intervals:
        extremum.append(intervals[0][1])
        for i in range(1, len(intervals)):
            if extremum[i - 1] > intervals[i][1]:
                extremum.append(extremum[i - 1])
            else:
                extremum.append(intervals[i][1])
    return extremum


def create_extremum_desc(intervals: List[List[int]]):
    extremum = []
    if intervals:
        extremum.append(intervals[len(intervals) - 1][0])
        for i in range(len(intervals) - 2, -1, -1):
            if extremum[-1] < intervals[i][0]:
                extremum.append(extremum[i - 1])
            else:
                extremum.append(intervals[i][0])
    return extremum[-1::-1]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        interval1 = intervals[0]
        left = []
        right = []
        extended_left = False
        extended_right = False
        for interval2 in intervals[1:]:
            if interval1[0] > interval2[1]:
                insert_idx = bin_search(left, interval2[1], 1, len(left))
                left.insert(insert_idx, interval2)
            elif interval1[1] < interval2[0]:
                insert_idx = bin_search(right, interval2[0], 0, len(right))
                right.insert(insert_idx, interval2)
            else:
                new_interval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
                if new_interval[0] != interval1[0]:
                    extended_left = True
                if new_interval[1] != interval1[1]:
                    extended_right = True
                interval1 = new_interval
        left_extremum = create_extremum_desc(left)
        right_extremum = create_extremum(right)
        interval1, right, right_extremum = self.extend_right_loop(extended_right, interval1, right, right_extremum)
        interval1, left, left_extremum = self.extend_left_loop(extended_left, interval1, left, left_extremum)
        result.append(interval1)
        while right:
            interval1 = right[0]
            right = right[0 + 1:]
            right_extremum = right_extremum[0 + 1:]
            interval1, right, right_extremum = self.extend_right_loop(True, interval1, right, right_extremum)
            result.append(interval1)
        while left:
            idx = len(left) - 1
            interval1 = left[idx]
            left = left[:idx]
            left_extremum = left_extremum[:idx]
            interval1, left, left_extremum = self.extend_left_loop(True, interval1, left, left_extremum)
            result.append(interval1)
        return result

    def extend_left_loop(self, extended_left, interval1, left, left_extremum):
        while extended_left and left:
            merge_idx = bin_search(left, interval1[0], 1, len(left) - 1)
            if interval1[0] <= left[merge_idx][1]:
                # if left_extremum[merge_idx] >= interval1[0]:
                #     extended_left = False
                interval1 = [min(interval1[0], left_extremum[merge_idx]), interval1[1]]
                left = left[:merge_idx]
                left_extremum = left_extremum[:merge_idx]
            else:
                extended_left = False
        return interval1, left, left_extremum

    def extend_right_loop(self, extended_right, interval1, right, right_extremum):
        while extended_right and right:
            merge_idx = bin_search2(right, interval1[1], 0, 0)
            if interval1[1] >= right[merge_idx][0]:
                # if right_extremum[merge_idx] <= interval1[1]:
                #     extended_right = False
                interval1 = [interval1[0], max(interval1[1], right_extremum[merge_idx])]
                right = right[merge_idx + 1:]
                right_extremum = right_extremum[merge_idx + 1:]
            else:
                extended_right = False
        return interval1, right, right_extremum


def call(intervals):
    s = Solution()
    return s.merge(intervals)


def test():
    assert call([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert call([[100, 200], [1, 5], [4, 7], [10, 20], [15, 101], [250, 260], [199, 250]]) == [
        [10, 260], [1, 7]
    ]
    assert call([[1, 5], [4, 7], [10, 20], [100, 200], [15, 101], [250, 260], [199, 250]]) == [
        [1, 7], [10, 260]
    ]
    assert call([[1, 5], [4, 7], [10, 20], [100, 200], [15, 101], [250, 260], [199, 250], [350, 350], [261, 350],
                 [350, 400]]) == [
               [1, 7], [10, 260], [261, 400]
           ]
    assert call([[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]) == [[2, 6], [1, 1], [0, 0]]
    assert call([[5, 5], [1, 3], [3, 5], [4, 6], [1, 1], [3, 3], [5, 6], [3, 3], [2, 4], [0, 0]]) == [[1, 6], [0, 0]]
    assert call([[5, 5], [1, 2], [2, 4], [2, 3], [4, 4], [5, 5], [2, 3], [5, 6], [0, 0], [5, 6]]) == [
        [5, 6], [1, 4], [0, 0]
    ]
    assert call([[3, 3], [1, 1], [0, 2], [2, 2], [1, 2], [1, 3], [1, 1], [3, 3], [2, 3], [4, 6]]) == [
        [5, 6], [1, 4], [0, 0]
    ]
