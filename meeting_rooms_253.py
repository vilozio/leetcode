from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_rooms = curr_rooms = 1  # 1, 2
        max_interval_end = 0  # 36
        min_interval_end = float('inf')  # 4
        intervals.sort(key=lambda x: x[0])
        for i, (_, i_end) in enumerate(intervals[:-1]):  # 34
            if min(i_end, min_interval_end) > intervals[i + 1][0]:  # 16, 20
                curr_rooms += 1
                max_interval_end = max(i_end, max_interval_end, intervals[i + 1][1])
                min_interval_end = min(i_end, min_interval_end, intervals[i + 1][1])
            elif max(i_end, max_interval_end) > intervals[i + 1][0]:
                min_interval_end = min(i_end, intervals[i + 1][1])
            else:
                min_rooms = max(min_rooms, curr_rooms)
                curr_rooms = 1
                max_interval_end = 0
                min_interval_end = float('inf')
        return max(min_rooms, curr_rooms)

# [[0, 1], [1, 5], [4, 5], [4, 10], [11, 12]]
# [[1, 3], [2, 10], [4, 6], [5, 7], [6, 8]]
# [[1, 3], [2, 10], [4, 6], [5, 7], [5, 8]]
