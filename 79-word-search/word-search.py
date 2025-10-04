class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(row, col, word):
            if len(word) == 0:
                return True
            
            if (row < 0 or rows == row or col < 0 or cols == col or board[row][col] != word[0]):
                return False
            
            board[row][col] = "#"
            for rowOffset, colOffset in [(0,1),(-1,0),(0,-1),(1,0)]:
                if backtrack(row + rowOffset, col + colOffset, word[1:]):
                    return True

            board[row][col] = word[0]
            return False 

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, word):
                    return True
        return False