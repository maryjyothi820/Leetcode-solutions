2856. Minimum Array Length After Pair Removals.py
class Solution:
    def minLengthAfterRemovals(self, nums):
        n = len(nums)

        maxFreq = 1
        count = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                maxFreq = max(maxFreq, count)
                count = 1

        maxFreq = max(maxFreq, count)

        if maxFreq > n // 2:
            return 2 * maxFreq - n
        else:
            return n % 2
        
