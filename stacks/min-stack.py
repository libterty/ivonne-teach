class MinStack(object):
  
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(len(self.stack) - 1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.pop()
print(minStack.stack)
