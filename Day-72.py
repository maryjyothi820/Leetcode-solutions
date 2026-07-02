1191. K-Concatenation Maximum Sum
class Solution:
    def kConcatenationMaxSum(self, arr, k):
        MOD = 10**9 + 7

        def kadane(nums):
            cur = best = 0
            for x in nums:
                cur = max(0, cur + x)
                best = max(best, cur)
            return best

        if k == 1:
            return kadane(arr) % MOD

        total = sum(arr)
        max2 = kadane(arr * 2)

        if total > 0:
            return (max2 + (k - 2) * total) % MOD
        else:
            return max2 % MOD
