494.Target_sum.py
class Solution:
    def findTargetSumWays(self, nums, target):

        dp = {0: 1}

        for num in nums:
            next_dp = {}

            for total in dp:
                plus = total + num
                minus = total - num

                next_dp[plus] = next_dp.get(plus, 0) + dp[total]
                next_dp[minus] = next_dp.get(minus, 0) + dp[total]

            dp = next_dp

        return dp.get(target, 0)