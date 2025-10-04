class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(i):
            res.append(sol[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                sol.append(nums[j])
                backtrack(j + 1)
                sol.pop()
        
        nums.sort()
        n = len(nums)
        res, sol = [], []
        backtrack(0)
        return res