class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        fal = []  # List to store indices where adjacent elements have the same parity
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:  # Check if adjacent elements have the same parity
                fal.append(i)
        
        # Initialize result array as True
        arr = [True] * len(queries)
        
        # If `fal` is empty, no queries need to be False
        if not fal:
            return arr
        
        # Process each query
        for i in range(len(queries)):
            s, e = queries[i][0], queries[i][-1]  # Extract start and end indices
            if s != e:  # Skip single-element queries
                idx = bisect.bisect_left(fal, s)  # Find the smallest index in `fal` >= `s`
                if idx < len(fal) and fal[idx] < e:  # Check if there's a problematic index in the range
                    arr[i] = False
        
        return arr