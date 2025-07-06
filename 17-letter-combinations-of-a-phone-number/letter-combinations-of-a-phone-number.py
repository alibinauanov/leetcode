class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numLet = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        letters = []
        for i in range(len(digits)):
            letters.append(numLet[digits[i]])

        def dfs(start, path):
            if start == len(letters):
                res.append("".join(path))
                return

            for ch in letters[start]:
                path.append(ch)
                dfs(start + 1, path)
                path.pop()
        
        if len(digits) == 0:
            return []

        dfs(0, [])
        return res