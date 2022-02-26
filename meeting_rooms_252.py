from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        for i, (_, i_end) in enumerate(intervals[:-1]):
            if i_end > intervals[i + 1][0]:
                return False
        return True

# [[0, 10], [11, 12], [20, 20]]
