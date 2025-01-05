class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        subarr1 = set()
        subarr2 = set()

        for i in nums1:
            if i not in nums2Set:
                subarr1.add(i)
        
        for i in nums2:
            if i not in nums1Set:
                subarr2.add(i)
        
        return [list(subarr1), list(subarr2)]