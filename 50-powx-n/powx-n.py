class Solution(object):
    def binaryExp(self, x, n):
        if n == 0:
            return 1
        
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)
        
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        else:
            return self.binaryExp(x * x, n // 2)

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return self.binaryExp(x, n)