import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        min_rooms = 1
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(heap, intervals[0][1])  # [(36, [2, 36])]
        for intr in intervals[1:]:  # [39, 46]
            if intr[0] >= heap[0]:  # 39 >= 20
                heapq.heappop(heap)  # [(34, [13, 34]), (36, [2, 36])]
            heapq.heappush(heap, intr[1])  # [(46, [39, 46]), (34, [13, 34]), (36, [2, 36])]
            min_rooms = max(min_rooms, len(heap))  # 3
        return min_rooms

# [[0, 1], [1, 5], [4, 5], [4, 10], [11, 12]]
# [[1, 3], [2, 10], [4, 6], [5, 7], [6, 8]]
# [[1, 3], [2, 10], [4, 6], [5, 7], [5, 8]]
