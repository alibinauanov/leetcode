class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        mp = {}
        l = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]])
            ans = max(ans, r - l + 1)
            mp[s[r]] = r + 1
        return ans