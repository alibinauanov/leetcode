class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        pointer1 = 0
        pointer2 = 0

        while len(nums1) > pointer1 and len(nums2) > pointer2:
            if nums1[pointer1] <= nums2[pointer2]:
                nums.append(nums1[pointer1])
                pointer1 += 1
            else:
                nums.append(nums2[pointer2])
                pointer2 += 1
        
        if pointer1 < len(nums1):
            nums.extend(nums1[pointer1:])
        if pointer2 < len(nums2):
            nums.extend(nums2[pointer2:])

        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2.0
        else:
            return float(nums[mid])