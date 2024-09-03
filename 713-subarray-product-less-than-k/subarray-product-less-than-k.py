class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [10, 5, 2, 6] => [10], [5], [2], [6], [10, 5], [5, 2], [5, 2, 6], [2, 6]
        if k <= 1:
            return 0

        product = 1
        l = 0
        counter = 0

        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product /= nums[l]
                l += 1
            counter += r - l + 1

        return counter