class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = []
        n1 = 0
        n2 = 0

        while len(nums1) > n1 and len(nums2) > n2:
            if nums1[n1] <= nums2[n2]:
                merge.append(nums1[n1])
                n1 += 1
            else:
                merge.append(nums2[n2])
                n2 += 1
        
        if len(nums1) > n1:
            merge.extend(nums1[n1:])
        if len(nums2) > n2:
            merge.extend(nums2[n2:])
        
        n = len(merge) // 2
        if len(merge) % 2 == 0:
            return (merge[n] + merge[n - 1]) / 2.0
        else:
            return float(merge[n])