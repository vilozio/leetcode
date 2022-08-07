from itertools import islice


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """The problem is solved with Pascal's triangle."""
        bl_corner = 1
        # br_corner = 2
        right_line = [1, 2]
        if m == 1 or n == 1:
            return 1
        if m == n == 2:
            return 2
        # Expand grid to bottom.
        for _ in range(m - 2):
            right_line.append(right_line[-1] + bl_corner)
            # br_corner += bl_corner
        for _ in range(n - 2):
            upper_cell = 1
            for i, cell in enumerate(right_line[1:]):
                right_line[i - 1] = upper_cell
                upper_cell += cell
            right_line[-1] = upper_cell
        return right_line[-1]

