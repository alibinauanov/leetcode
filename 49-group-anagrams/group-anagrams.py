class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
            
        for s in strs:
            sortedS = "".join(sorted(s))
            hashmap[sortedS].append(s)
        return list(hashmap.values())

        # {
        #     "aet": ["eat", "tea", "ate"],
        #     "ant": ["tan", "nat"],
        #     "aby": ["bat"]
        # }