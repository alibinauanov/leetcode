class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
        
        # # 0
        # leftSum = 1
        # rightSum = 27
        # # 1
        # rightSum = 28 - 7 - 1 = 20
        # leftSum = 8
        # # 2
        # rightSum = 28 - 3 - 8 = 17
        # leftSum = 11
        # # 3
        # rightSum = 28 - 6 - 11 = 11
        # leftSum == rightSum: index 3
        # output: 3