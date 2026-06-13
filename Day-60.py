576:out_of_binary_paths
class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 1000000007
        memo = {}

        def dp(row, col, moves):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1

            if moves == 0:
                return 0

            if (row, col, moves) in memo:
                return memo[(row, col, moves)]

            ans = (
                dp(row + 1, col, moves - 1) +
                dp(row - 1, col, moves - 1) +
                dp(row, col + 1, moves - 1) +
                dp(row, col - 1, moves - 1)
            ) % MOD

            memo[(row, col, moves)] = ans
            return ans

        return dp(startRow, startColumn, maxMove)
