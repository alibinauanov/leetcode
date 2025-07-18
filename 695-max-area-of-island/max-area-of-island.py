class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            # to do
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            area = 1

            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            return area
        
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea