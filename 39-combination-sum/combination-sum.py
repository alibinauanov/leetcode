class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        return res