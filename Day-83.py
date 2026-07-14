2008. Maximum Earnings From Taxi.py
class Solution:
    def maxTaxiEarnings(self, n, rides):

        from bisect import bisect_left

        # Store rides by start point
        rides.sort()

        starts = []
        for ride in rides:
            starts.append(ride[0])

        m = len(rides)

        dp = [0] * (m + 1)

        for i in range(m - 1, -1, -1):

            start, end, tip = rides[i]

            # Find next ride whose start >= current end
            next_index = bisect_left(starts, end)

            take = (end - start + tip) + dp[next_index]

            skip = dp[i + 1]

            dp[i] = max(take, skip)

        return dp[0]
        
