2537. Count the Number of Good Subarrays.py
from collections import defaultdict

class Solution:
    def countGood(self, nums, k):
        freq = defaultdict(int)
        left = 0
        pairs = 0
        ans = 0
        n = len(nums)

        for right in range(n):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while pairs >= k:
                ans += n - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return ans
