class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr_num = 0
        res = ""
        stack = []

        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            elif s[i] == "[":
                stack.append(curr_num)
                stack.append(res)
                curr_num = 0
                res = ""
            elif s[i] == "]":
                res = stack.pop() + res * stack.pop()
            else:
                res += s[i]
        return res