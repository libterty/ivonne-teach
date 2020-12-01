# Input: s = "()[]{}"
# Output: true

# Input: s = "([)]"
# Output: false

class Solution(object):
    # map is better
    # def switch(self, i):
    #     switcher = {
    #         0: "(",
    #         1: ")",
    #         2: "{",
    #         3: "}",
    #         4: "[",
    #         5: "]"
    #     }
    #     return switcher.get(i, "switcher")

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        stack = []
        maps = {
          ")": "(",
          "}": "{",
          "]": "["
        }
        for i in s:
            if i not in maps:
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != maps[i]:
                return False
        return len(stack) == 0


print(Solution().isValid("([)]"))
print(Solution().isValid("()[]{}"))