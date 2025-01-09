class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = []
        for i in range(len(s)):
            if s[i] != "*":
                new_s.append(s[i])
            else:
                new_s.pop()
        return "".join(new_s)