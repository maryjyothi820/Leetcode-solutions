961. N-Repeated Element in Size 2N Array.py
class Solution:
    def repeatedNTimes(self, nums):

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            # repeated element found
            if freq[num] > 1:
                return num
