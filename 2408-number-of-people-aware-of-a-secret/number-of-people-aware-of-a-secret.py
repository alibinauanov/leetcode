class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        know, share = deque([(1, 1)]), deque([])
        knowCnt, shareCnt = 1, 0
        for i in range(2, n + 1):
            if know and know[0][0] == i - delay:
                knowCnt -= know[0][1]
                shareCnt += know[0][1]
                share.append(know[0])
                know.popleft()
            if share and share[0][0] == i - forget:
                shareCnt -= share[0][1]
                share.popleft()
            if share:
                knowCnt += shareCnt
                know.append((i, shareCnt))
        return (knowCnt + shareCnt) % (10**9 + 7)