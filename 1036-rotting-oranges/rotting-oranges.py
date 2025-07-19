class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Find all rotten and fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minutes)
                elif grid[r][c] == 1:
                    fresh += 1

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        minutes = 0
        rotted = 0

        # Step 2: BFS
        while queue:
            r, c, minute = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # rot the orange
                    rotted += 1
                    queue.append((nr, nc, minute + 1))
                    minutes = minute + 1

        return minutes if rotted == fresh else -1