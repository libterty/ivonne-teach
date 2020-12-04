import collections

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        num_len = len(nums)
        dp = [collections.defaultdict(int) for _ in range(num_len + 1)] 
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[num_len][S]

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))