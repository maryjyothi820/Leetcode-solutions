2708:max_strenght_of_a_group
class Solution:
    def maxStrength(self, nums):
        n = len(nums)
        ans = float('-inf')

        for mask in range(1, 1 << n):
            product = 1

            for i in range(n):
                if mask & (1 << i):
                    product *= nums[i]

            ans = max(ans, product)

        return ans
