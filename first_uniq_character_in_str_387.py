class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_met = [-1 for _ in range(26)]
        count = [0 for _ in range(26)]
        ascii_start = ord('a')
        for i, c in enumerate(s):
            position = ord(c) - ascii_start
            if first_met[position] == -1:
                first_met[position] = i
            count[position] += 1
        once_idxs = (i for i, c_count in enumerate(count) if c_count == 1)
        min_idx = float('inf')
        for i in once_idxs:
            if first_met[i] < min_idx:
                min_idx = first_met[i]
        if min_idx == float('inf'):
            return -1
        return min_idx


# s         - 'ababc'
# first_met - [0, 1, 4]
# count     - [2, 2, 1]
#
# i, c      - 4, c
# position  - 2
# once_idxs - (2)
