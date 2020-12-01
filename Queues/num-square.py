# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp is a list structure represents the perfect sqaure which required to compostie a perfect sqaures 
        dp = [n] * (n + 1)
        # start with 0 and 1
        dp[0] = 0
        dp[1] = 1
        # looping from third el
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]




print(Solution().numSquares(13))
print(Solution().numSquares(12))