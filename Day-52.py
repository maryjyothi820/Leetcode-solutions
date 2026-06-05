377.Combination_sum_4
class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1

        for t in range(1, target + 1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]

        return dp[target]
1035.Uncrossed_lines
class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]