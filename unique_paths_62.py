class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """The problem is solved with Pascal's triangle.
        
        Each sell contains number of unique paths to it.
        
        Using bottom-up approach, we start with a 2x2 grid
        
          1  1
          1  2
          
        And expand it first to the bottom, then to the right.
        We keep only right most line of the grid, because we need
        only the right bottom corner.
        """
        bl_corner = 1
        right_line = [1, 2]
        if m == 1 or n == 1:
            return 1
        if m == n == 2:
            return 2
        # Expand grid to bottom.
        for _ in range(m - 2):
            right_line.append(right_line[-1] + bl_corner)
        # Expand grid to right.
        for _ in range(n - 2):
            upper_cell = 1
            for upper_i, cell in enumerate(right_line[1:]):
                right_line[upper_i] = upper_cell
                upper_cell += cell
            right_line[-1] = upper_cell
        return right_line[-1]
