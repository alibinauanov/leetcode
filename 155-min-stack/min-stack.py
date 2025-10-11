class MinStack(object):

    # initialize: stack = []
    # push: stack.append(val)
    # pop: stack.pop()
    # top: return stack[-1]

    def __init__(self):
        self.arr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.arr:
            self.arr.append((val, val))
            return
        currMin = self.arr[-1][1]
        self.arr.append((val, min(val, currMin)))

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()