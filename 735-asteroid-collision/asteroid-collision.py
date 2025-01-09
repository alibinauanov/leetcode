class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                res.append(asteroids[i])
            else:
                while res and res[-1] > 0:
                    if res[-1] < abs(asteroids[i]):
                        res.pop()
                    elif res[-1] == abs(asteroids[i]):
                        res.pop()
                        break
                    else:
                        break
                else:
                    res.append(asteroids[i])
        return res

        # if negative asteroid explode the positive asteroid on the left,
        # then check the next positive asteroid as it can be exploded as well