974. Subarray Sums Divisible by K.py
class Solution:
    def subarraysDivByK(self, nums, k):

        prefix = 0
        count = 0

        freq = {0:1}

        for num in nums:

            prefix += num

            rem = prefix % k

            count += freq.get(rem,0)

            freq[rem] = freq.get(rem,0)+1

        return count
