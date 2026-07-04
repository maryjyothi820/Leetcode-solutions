2170. Minimum Operations to Make the Array Alternating.py
from collections import Counter

class Solution:
    def minimumOperations(self, nums):
        n = len(nums)

        if n == 1:
            return 0

        even = Counter(nums[::2])
        odd = Counter(nums[1::2])

        even_common = even.most_common(2)
        odd_common = odd.most_common(2)

        if len(even_common) == 1:
            even_common.append((0, 0))
        if len(odd_common) == 1:
            odd_common.append((0, 0))

        even_val1, even_cnt1 = even_common[0]
        even_val2, even_cnt2 = even_common[1]

        odd_val1, odd_cnt1 = odd_common[0]
        odd_val2, odd_cnt2 = odd_common[1]

        even_size = (n + 1) // 2
        odd_size = n // 2

        if even_val1 != odd_val1:
            return (even_size - even_cnt1) + (odd_size - odd_cnt1)

        ans1 = (even_size - even_cnt1) + (odd_size - odd_cnt2)
        ans2 = (even_size - even_cnt2) + (odd_size - odd_cnt1)

        return min(ans1, ans2)
        
