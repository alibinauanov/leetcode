class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r, d = deque(), deque()
        for i, s in enumerate(senate):
            if s == "R":
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            radiant = r.popleft()
            dire = d.popleft()

            if radiant < dire:
                r.append(radiant + len(senate))
            else:
                d.append(dire + len(senate))
            
        return "Radiant" if r else "Dire"

        # RDD
        # r = [3]
        # d = [2]

        # while:
        #     1)radiant = 0; dire = 1
        #     0 < 1:
        #         r = 3
        #     2)radiant = 3; dire = 2
        #     3 > 2:
        #         d = 5