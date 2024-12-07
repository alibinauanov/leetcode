class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            
            # Check if there is an overlap
            if last[1] >= current[0]:
                # Merge the current interval with the last merged interval
                merged[-1] = [last[0], max(last[1], current[1])]
            else:
                # No overlap, add the current interval to merged list
                merged.append(current)
        
        return merged