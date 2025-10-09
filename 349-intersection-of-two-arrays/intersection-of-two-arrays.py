class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        n1 = set(nums1)
        for i in range(len(nums2)):
            if nums2[i] in n1 and nums2[i] not in ans:
                ans.append(nums2[i])
        return ans