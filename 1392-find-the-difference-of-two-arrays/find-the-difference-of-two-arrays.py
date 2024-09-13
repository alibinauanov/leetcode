class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_one, set_two = set(nums1), set(nums2)
        return [list(set_one - set_two), list(set_two - set_one)]