2304:min_path_cost_in_a_grid
class Solution:
    def minPathCost(self, grid, moveCost):
        m = len(grid)
        n = len(grid[0])

        dp = grid[0][:]

        for i in range(m - 1):
            new_dp = [float('inf')] * n

            for j in range(n):
                for k in range(n):
                    cost = dp[j] + moveCost[grid[i][j]][k] + grid[i + 1][k]
                    new_dp[k] = min(new_dp[k], cost)

            dp = new_dp

        return min(dp)
