2780. Minimum Index of a Valid Split.py
class Solution:
    def minimumIndex(self, nums):
        # Step 1: Find dominant element
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Step 2: Count total occurrences
        total = nums.count(candidate)
        n = len(nums)

        leftCount = 0

        # Step 3: Find minimum valid split
        for i in range(n - 1):
            if nums[i] == candidate:
                leftCount += 1

            leftSize = i + 1
            rightSize = n - leftSize
            rightCount = total - leftCount

            if leftCount * 2 > leftSize and rightCount * 2 > rightSize:
                return i

        return -1
        
