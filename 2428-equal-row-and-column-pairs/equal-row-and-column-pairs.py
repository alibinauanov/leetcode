class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid2 = []
        for i in range(len(grid[0])):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            grid2.append(column)
        
        counter = 0
        
        # Count each row in grid that matches any column in grid2
        for row in grid:
            counter += grid2.count(row)
        
        return counter
        
        # take every i_th element of every subarray to construct the grid of columns [DONE]
        # we already have grid of rows [DONE]
        # then we can compare it like: [DONE]
        # if grid[i] in grid2: [DONE]
        #   counter += 1 [DONE]
        # return counter [DONE]