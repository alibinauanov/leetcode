class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums = sorted(nums)
        # return nums[len(nums) - k:]

        # Pair each number with its index
        indexed = [(nums[i], i) for i in range(len(nums))]

        # Get k largest values by value (descending)
        top_k = sorted(indexed, reverse=True)[:k]

        # Sort those k elements by original index to keep subsequence order
        top_k.sort(key=lambda x: x[1])

        # Extract the values only
        return [x[0] for x in top_k]