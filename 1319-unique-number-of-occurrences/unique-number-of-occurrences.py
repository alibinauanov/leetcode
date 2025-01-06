class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = Counter(arr)
        values = counts.values()
        unique_values = set(values)
        return len(values) == len(unique_values)

        # (key, value)
        # for i in range(len(arrSet)):
        #   if key's value in arrSet's values:
        #       return False
        #   else:
        #       return True