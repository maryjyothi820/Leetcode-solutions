873. Length of Longest Fibonacci Subsequence.py
class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)

        index = {}

        for i in range(n):
            index[arr[i]] = i

        dp = [[2] * n for _ in range(n)]

        ans = 0

        for i in range(n):
            for j in range(i):

                prev = arr[i] - arr[j]

                if prev < arr[j] and prev in index:

                    k = index[prev]

                    dp[j][i] = dp[k][j] + 1

                    ans = max(ans, dp[j][i])

        return ans if ans >= 3 else 0
