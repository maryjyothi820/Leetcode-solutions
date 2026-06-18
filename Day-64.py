539.minimum_time_difference.py
class Solution:
    def findMinDifference(self, timePoints):
        minutes = []

        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)

        minutes.sort()

        ans = float('inf')

        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])

        ans = min(ans, 1440 - minutes[-1] + minutes[0])

        return ans
