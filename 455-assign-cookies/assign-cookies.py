class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_point = 0
        s_point = 0
        counter = 0
        
        while g_point < len(g):
            while s_point < len(s):
                if g[g_point] <= s[s_point]:
                    counter += 1
                    s_point += 1
                    break
                s_point += 1
            g_point += 1
        return counter