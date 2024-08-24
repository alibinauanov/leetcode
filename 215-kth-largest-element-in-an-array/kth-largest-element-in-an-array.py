class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # SORT APPROACH
        nums.sort(reverse=True)
        return nums[k-1]

        # k = len(nums) - k

        # def quickSelect(l, r):
        #     pivot, p = nums[r], l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if p > k:   return quickSelect(l, p - 1) 
        #     elif p < k: return quickSelect(p + 1, r)
        #     else:       return nums[p]
        
        # return quickSelect(0, len(nums) - 1)