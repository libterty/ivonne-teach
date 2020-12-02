# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
import math

class Solution(object):
    def __init__(self):
        self.operators = {
          "+",
          "-",
          "/",
          "*"
        }

    def calc(self, operator, first, next):
        if operator == "+":
            return first + next
        elif operator == "-":
            return first - next
        elif operator == "*":
            return first * next
        else:
            # python 2.7 is integer divsion it will calcuate error
            return int(float(first) / next)

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for el in tokens:
            # move all number to stack
            if el not in self.operators:
                stack.append(int(el))
                continue
            # remove number with stack
            next = stack.pop(-1)
            first = stack.pop(-1)
            stack.append(self.calc(el, first, next))
        return stack[0]


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))
