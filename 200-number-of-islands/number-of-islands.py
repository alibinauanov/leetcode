class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 1 1 0 0 0   +1
        # 1 1 0 0 0   +0
        # 0 0 1 0 0   +1
        # 0 0 0 1 1   +1
        #             =3

        # check the indexes of every row and column

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            # to do
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != "1":
                return
            grid[r][c] = "#"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count