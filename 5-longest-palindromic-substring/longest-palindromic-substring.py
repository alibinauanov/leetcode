class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        ans = [0, 0]

        for i in range(len(s)):
            oddLen = expand(i, i)
            if oddLen > ans[1] - ans[0] + 1:
                dist = oddLen // 2
                ans = [i - dist, i + dist]
            
            evenLen = expand(i, i + 1)
            if evenLen > ans[1] - ans[0] + 1:
                dist = (evenLen // 2) - 1
                ans = [i - dist, i + 1 + dist]
        
        i, j = ans
        return s[i:j+1]